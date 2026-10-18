"""Independent checks of the joint linear complexity / discrepancy distribution."""
from verify_fsr import period,lc,discrepancy
from verify_euler import main as euler
from collections import Counter
EXPECTED={21:[0, 0, 8, 0],22:[0, 0, 0, 0],23:[4, 4, 4, 0],24:[0, 12, 4, 4],25:[10, 10, 12, 0],26:[4, 8, 16, 8],27:[10, 22, 28, 4],28:[28, 56, 88, 8],29:[24, 96, 72, 32],30:[52, 156, 184, 56],31:[92, 324, 496, 112]}

def main():
    first=Counter()
    for fb in range(1<<16):
        seq=period(fb)
        if seq is not None:first[lc(seq),discrepancy(seq)]+=1
    second=euler()
    expected={(lin,d):count for lin,counts in EXPECTED.items() for d,count in zip((5,6,7,8),counts) if count}
    assert first==expected,(first,expected)
    assert second==expected,(second,expected)
    assert sum(first.values())==2048
    assert first[31,5]==92
    assert [sum(first[lin,d] for lin in EXPECTED) for d in (5,6,7,8)]==[224,688,912,224]
    print('FBS_OK',len(first),'nonzero_cells=34')
    print('JOINT_OK jointly_min_discrepancy_and_max_linear_complexity=92')
if __name__=='__main__':main()
