# Independent mathematical audit

## correctness

PASS

Durham's Theorem 2 gives obstructions 4^j(16h+14), whose valuations are 2j+1. Sobolewski–Ulas Proposition 3.1 confines the values b(2n) to valuations 1 and 2, so only b(2n)≡14 mod 16 is needed. I checked the exact published congruences in Propositions 3.2 and 3.7. The first relation of Prop. 3.7 as printed is not used (at n=0 it would incorrectly identify b(8)=10 with b(2)=2 mod 16). The elementary recurrence b(2k)−b(2k−2)=b(k), together with b(2k+1)=b(2k), gives b(16v+8)=b(16v+4)+b(8v+2)+b(8v+4). Applying the cited usable relations at v=2m and v=2m+1 yields the required shift by 8 modulo 16 in both cases, and b(16m)≡b(4m) propagates the shift to all higher even-valuation layers. The two selected odd residues per sign and the disjoint scaled-layer count then follow. I independently reconstructed the 16 weights as 6·1_{4p+r≥3 or 7 according to sign}−3p−r and verified both potential inequalities and the terminal offsets with `python3 /workspace/review-evidence/binary_digit.py`; that script also checks 8192 residues using the partition Euler product rather than the recurrence. The upper potential gives D≤7, with four exceptions through 17. For the lower bound, the reduced weights e+3 admit a lower potential and telescope to d(Y)≥−3 times the number of base-four digits minus 1. In state order (0,+),(0,−),(1,+),(1,−), the witness Y with digits 2(12)^k11 starts with weight −2, traverses k cycles of weights −1,−5, and terminates with weights −1,−4 at (1,+). Appending 0 gives X=(768·16^k−28)/5 and offset −3, hence D(X)=−10−6k and the exact liminf −1/4 after normalization. The bounds prove density 1/6 for exceptions; the finite coefficient check is corroboration, not the all-index argument.

## originality

PASS

The distinct result is the weighted-form sharp all-cutoff discrepancy bound with an attaining index and the exact negative logarithmic liminf. The digit criterion is a near consequence of cited valuation/congruence ingredients and the known representation obstruction; the originating paper even names this weighted form as an extension. It is not credited here as a stand-alone originality claim. The closest three-square results have different exceptional sets and do not give the weighted-form sharp constants.

## value

PASS

This is a weighted form explicitly suggested in the originating partition study. Its distribution differs in a substantive way from density alone: the positive discrepancy is uniformly bounded and attained, whereas negative excursions reach logarithmic size with an exact coefficient. The attaining digit path and potential bound explain the asymmetry rather than merely approximating it in a count table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
