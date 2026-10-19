"""Recompile two independent exhaustive engines and check the run-merger theorem."""
from pathlib import Path
import re
import subprocess
import sys
import tempfile

EXPECTED_COUNTS = (1, 7, 36, 171, 813, 4012, 20891, 115463, 677546, 4211549)
WITNESS = '001101121122'


def main():
    folder = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as tmp:
        executables = []
        for name in ('verify_fast.cpp', 'verify_independent.cpp'):
            exe = Path(tmp) / name.removesuffix('.cpp')
            subprocess.run(['g++', '-std=c++17', '-O3', '-o', str(exe), str(folder / name)], check=True)
            executables.append(exe)
        for n in range(3, 13):
            output_fast = subprocess.check_output([str(executables[0]), str(n), str(n)], text=True)
            output_ind = subprocess.check_output([str(executables[1]), str(n)], text=True)
            fast = re.search(r'n=(\d+) checked=(\d+) bad=(\d+)', output_fast)
            ind = re.search(r'INDEPENDENT_N=(\d+) CHECKED=(\d+) BAD=(\d+) WITNESS=(\w+)', output_ind)
            assert fast and ind, (n, output_fast, output_ind)
            count = EXPECTED_COUNTS[n - 3]
            bad = int(n == 12)
            assert tuple(map(int,fast.groups())) == (n,count,bad),(n,fast.groups())
            assert tuple(map(int,ind.groups()[:3])) == (n,count,bad),(n,ind.groups())
            assert ind.group(4) == (WITNESS if n == 12 else 'none'),(n,ind.group(4))
            if n == 12:
                assert 'bad='+WITNESS in output_fast, output_fast
    subprocess.run([sys.executable, str(folder / 'verify_family.py')], check=True)
    print('VERIFY_OK all canonical words with >=3 letters through length 12; unique witness at 12')


if __name__ == '__main__':
    main()
