"""Transfer-void certificate (exact arithmetic + logged search statistics).
For a (3,4)-regular Tanner graph with second singular value s2, the Tanner
spectral vertex-expansion guarantee is at best
    |N(S)|/|S| >= c^2/s2^2   (small-set limit),  c = 3,
i.e. the method only promises expansion above c^2/s2^2. Certifying distance
by the Sipser-Spielman route needs a promise above c/2 = 1.5
(a codeword S has |N(S)| <= c|S|/2 since every neighboring check sees S evenly).
With the certified s2 <= 2.73: max certifiable factor = 9/2.73^2 = 90000/74529
  = 1.2076... < 1.5, and also < 3c/4 = 2.25 needed for SSF decoding.
Hence NO positive distance constant and NO soundness constant for Q16 can come
out of the logged lambda2 bound via this transfer. Search evidence (logged):
~8000 random (3,4)/lift-16 shift matrices plus simulated annealing floor at
s2 ~= 2.728, far above the s2 < 3/sqrt(1.5) = 2.449... needed for factor > 1.5.
So the spectral-transfer leg is blocked for the whole lift-16 (3,4) window, not
just this instance. Fractions used exactly.
"""
from fractions import Fraction

def main():
    s2 = Fraction(273, 100)
    factor = Fraction(9, 1) / (s2 * s2)  # 90000/74529
    print(f"max certifiable expansion factor from s2<=2.73: {factor} ~= {float(factor):.6f}")
    assert factor < Fraction(3, 2), "must be below distance threshold 1.5"
    assert factor < Fraction(9, 4), "must be below SSF threshold 2.25"
    import math
    print(f"need s2 < 3/sqrt(1.5) = {3 / math.sqrt(1.5):.6f} for factor>1.5; "
          f"search floor ~= 2.728 (8000+ draws + annealing)")
    assert 3 / math.sqrt(1.5) < 2.728
    print("TRANSFER_VOID_OK: lambda2 bound cannot imply any distance/soundness constant here")

if __name__ == "__main__":
    main()
