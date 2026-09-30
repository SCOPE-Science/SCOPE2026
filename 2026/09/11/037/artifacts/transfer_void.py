"""Corrected transfer arithmetic for the certified Q16 instance.

`check_270.py` proves exactly that the second singular value s2 is > 2.70.
For the particular Tanner transfer expression c^2/s2^2 with c=3, this lower
bound gives the required *upper* bound

    9/s2^2 < 9/2.70^2 = 100/81 < 3/2.

Therefore that specific transfer expression cannot meet the 3/2 distance
threshold (and hence cannot meet the larger 9/4 SSF threshold).  This script
does not claim that every spectral argument, or every non-spectral argument,
is impossible.
"""
from fractions import Fraction


def main():
    s2_lower = Fraction(27, 10)
    factor_upper = Fraction(9, 1) / (s2_lower * s2_lower)
    assert factor_upper == Fraction(100, 81)
    assert factor_upper < Fraction(3, 2)
    assert factor_upper < Fraction(9, 4)
    print(f"check_270 certificate: s2 > 2.70")
    print(f"therefore 9/s2^2 < 100/81 ~= {float(factor_upper):.6f} < 1.5 < 2.25")
    print("TRANSFER_VOID_OK: this c^2/s2^2 transfer cannot reach the distance/SSF thresholds for the logged instance")


if __name__ == "__main__":
    main()
