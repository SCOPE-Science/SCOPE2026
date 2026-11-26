# One nested secant interval gives a nonreal pair on Gr(2,6)

## Finding

For eight simple Schubert divisors on \(\mathrm{Gr}(2,6)\), one pair of nested secancy intervals suffices for failure of total reality, even when all 32 rational secancy parameters are distinct. The overlapping example below has exactly 14 complex solutions, all transverse: 12 real points and one nonreal conjugate pair. A specified disjoint-interval comparison instance has exactly 14 transverse real solutions. The disjoint case is a control, not a new general all-reality theorem. The claim does not quantify a smallest overlap length or describe a transition along an entire deformation.

## Assumptions and parameters

Use the real rational normal curve \(\gamma(t)=(1,t,t^2,t^3,t^4,t^5)\) and the Schubert divisor \(\{H:H\cap K_i\ne0\}\), where \(K_i\) is the four-plane spanned by the four curve points in group \(i\). The secancy interval is the ordinary real interval between the smallest and largest parameters in the group. Group indices start at zero.

In instance A, group \(i\) is \(\{-7/5+2i/5+2j/25 : j=0,1,2,3\}\), for \(0\le i\le7\). In instance B retain these groups except for the following replacements:

| Index | Parameters |
|---|---|
| 3 | \(6/25,13/50,7/25,3/10\) |
| 4 | \(1/25,4/25,11/25,3/5\) |
| 5 | \(61/100,17/25,19/25,21/25\) |

The only overlap is the interval \((6/25,3/10)\) nested strictly inside \((1/25,3/5)\), of intersection length \(3/50\). All 32 parameters in each instance are pairwise distinct. Instance B is the one specified by the rational group table in the original data.

## Proof

**Equations.** For the parameters of group \(i\), form \(p_i(T)=\prod_j(T-t_{ij})\). The coefficient vectors \(a_i,b_i\) of \(p_i(T),Tp_i(T)\), padded to length six, span \(K_i^\perp\). Thus in Plücker coordinates \(P_{rs}\), indexed by \(0\le r<s\le5\), the divisor equation is \(\sum_{r<s}(a_{ir}b_{is}-a_{is}b_{ir})P_{rs}=0\). In the chart \(P_{01}\ne0\) write \(H=[I_2\mid M]\); substituting its minors gives eight quadratic equations \(F(M)=0\) in eight unknowns. This construction is equivalent to the determinant of the six-row matrix formed by stacking a basis of \(H\) over the four rows \(\gamma(t_{ij})\).

**Local certificates.** Use the complex coordinate supremum norm with ordinary complex modulus on each coordinate. For each rational complex center \(x\) and rational complex preconditioner \(Y\), write \(J=F'(x)\) and \(F(x+u)=F(x)+Ju+H_2(u,u)\). Let \(e\), \(b\), and \(h\) be rational upper bounds on \(\|I-YJ\|_\infty\), \(\|YF(x)\|_\infty\), and the bilinear norm of \(YH_2\), respectively. The bounds use rational upward rounding of complex moduli. On the ball of radius \(r=10^{-6}\), the map \(z\mapsto z-YF(z)\) has derivative norm at most \(q=e+2rh\). The checker verifies \(q<1\) and \(b+qr<r\), so the ball contains a unique fixed point. Both \(Y\) and the Jacobian at the fixed point are invertible by the norm bounds on \(I-YF'(z)\); the fixed point is a simple zero. Real centers give real roots by conjugation and uniqueness. In B the two nonreal centers have an imaginary component exceeding the ball radius; their roots are therefore nonreal. The 14 balls in each instance are pairwise disjoint, with certified center separation exceeding 0.2975 in A and 0.3318 in B.

One may also bound the Euclidean Smale \(\alpha\): \(\|J^{-1}F(x)\|_2\le\sqrt8\,b/(1-e)\) and the Euclidean bilinear norm of \(J^{-1}H_2\) is at most \(\sqrt8\,h/(1-e)\). Since the system is quadratic this gives \(\alpha_2\le 8bh/(1-e)^2\), checked below \(4.3\cdot10^{-9}\) in A and \(1.2\cdot10^{-2}\) in B. The simple-root and reality conclusions use the direct contraction bounds and do not depend on rounding a Smale threshold.

**Global count.** To exclude the complement \(P_{01}=0\), append that equation to the eight divisor forms. Modulo the prime 1009 these nine forms have rank nine in both instances, with no denominators divisible by 1009. Eliminate the nine pivot variables and substitute the remaining six coordinates into the 15 Plücker quadrics. Products of these quadrics by all degree-two monomials span the entire degree-four space: the matrix rank is 126 in each instance, equal to the number of degree-four monomials in six coordinates. The elimination lifts over the rationals localized at 1009 and the full-rank minors are nonzero in characteristic zero. Hence every degree-four monomial belongs to the reduced characteristic-zero ideal. No point of the complex projective solution set lies on \(P_{01}=0\). The entire intersection is projective and contained in an affine chart, hence is zero-dimensional. A proper intersection of these eight hyperplane sections has length \(\deg\mathrm{Gr}(2,6)=14\) in the Plücker embedding. The 14 simple zeros already certified exhaust it. Conjugation now pairs the only two nonreal roots in B.

## Verification and scope

Run `python3 check_secant.py` with NumPy and SymPy. The script constructs the equations from the stated rational parameters, finds candidate centers, rationalizes them and their preconditioners, and checks every local inequality exactly. The floating-point search only supplies centers; neither exhaustion nor transversality follows from the search. For each case it prints modular ranks `9 126`, and reports the certified real/nonreal counts `14 0` and `12 2` respectively. The result establishes failure with one nested pair in this particular Schubert problem. It does not establish any necessary or sufficient condition for total reality with overlaps in general.

## Context

The disjoint instance is covered by Karp–Purbhoo's divisor secant theorem (Theorem 1.8). García-Puente et al., Table 5, already observed 12-real instances of this same degree-14 Schubert problem, including at overlap number 3 as well as 4. Their overlap number is a point-in-interval statistic minimized over choices of cut of the real projective line, not a count of overlapping pairs. For the parameters above it is 4: at the cut at infinity the four points of group 3 are the only contributions; a cut inside the wide interval makes its spanning interval include the other six groups, while a cut outside it preserves these four contributions. The printed table does not specify the single-nested geometry of its 12-real cases. The point here is the explicit jointly disjoint point sets and the single nested pair of intervals, with exact local and global certification, not a first observation of overlap-associated nonreality or a minimal overlap number.

- L. García-Puente et al., *The Secant Conjecture in the real Schubert calculus*, [arXiv:1010.0665](https://arxiv.org/abs/1010.0665).
- N. Hein et al., *The monotone secant conjecture in the real Schubert calculus*, [arXiv:1109.3436](https://arxiv.org/abs/1109.3436).
- J. D. Hauenstein, N. Hein, F. Sottile, *A primal-dual formulation for certifiable computations in Schubert calculus*, [arXiv:1406.0864](https://arxiv.org/abs/1406.0864).
- S. N. Karp, K. Purbhoo, *Universal Plücker coordinates for the Wronski map and positivity in real Schubert calculus*, [arXiv:2309.04645](https://arxiv.org/abs/2309.04645).
