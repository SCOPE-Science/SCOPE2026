# Verify support bound implies 2i+3 range dominates and 2i+2 maps are stable for i>=2.
def bound(d):
    # floor(2d/3)+4
    return (2*d)//3 + 4

print("d : bound(d), 2d+3, 2d+2, range_ok?, sharp_stable?")
for d in range(0,15):
    b=bound(d)
    r=2*d+3
    s=2*d+2
    # range requires r>=b except d=0 handled separately
    # sharp stability requires s>=b (for d>=2) or direct check for d<2
    print(f"{d:2d} : bound={b:2d}, 2d+3={r:2d} ({r>=b}), 2d+2={s:2d} ({s>=b})")

# Direct checks: H0 coinvariants vanish for k>=3 (character/integer linear algebra already in char_dims.py, stab_q4.py)
# H1/H2/H3 vanish because H^1(F_k)=0, H^2\otimes W invariants vanish, H^3 invariants vanish (explore_h4.py Gram=0).
# Print summary
print("i=0: k>=3 maps 0->0 iso (W2=0, coinvariants 0 for k>=3).")
print("i=1: H1(F_k)=0 => twisted H1=0 for all k, maps 0->0 iso (includes k=4->5 at 2i+2=4).")
