"""Compare the exact optimum masks computed in the two graph presentations."""
import json,sys
if len(sys.argv)!=3:
    raise SystemExit('usage: python3 crosscheck.py certificate.json verify_petersen.output.txt')
with open(sys.argv[1],encoding='utf8') as f:C=json.load(f)
with open(sys.argv[2],encoding='utf8') as f:S=f.read()
needle='mapped_H5_masks='
assert S.count(needle)==1
mapped=list(map(int,S.split(needle)[1].splitlines()[0].split(',')))
assert sorted(mapped)==C['optimal_states']
assert len(mapped)==len(set(mapped))==155
print('OPTIMAL_MASKS_EXACTLY_AGREE 155')
