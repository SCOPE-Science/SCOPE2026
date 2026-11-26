# Exact ordered two-summand counts over dyadic residue rings

## Finding

Fix an integer \(t\ge2\) and put \(d=2^t\), \(h=t+2\). For \(n\ge0\), let \(R_{t,n}(r)\) count **ordered** pairs \((x,y)\) modulo \(q=2^n\) with \(x^d+y^d\equiv r\pmod q\). Then:

* For \(n=0\), \(R_{t,0}(0)=1\). For \(n=1\), each of the two targets has count \(2\).
* For \(2\le n<h\), the targets \(0,1,2\) have counts \(q^2/4,q^2/2,q^2/4\), respectively; the other counts are zero.
* For \(n\ge h\), the counts for targets congruent to \(1\) or \(2\) modulo \(2^h\) are \(2^{t+1}q\) and \(2^tq\), respectively.
* For \(h\le n<d\), the only remaining nonzero count is \(R_{t,n}(0)=q^2/4\).
* For \(n\ge d\), every target outside the two stated classes modulo \(2^h\) has count
  \[
  R_{t,n}(r)=
  \begin{cases}
   2^{2(d-1)} R_{t,n-d}(r/2^d),& r\equiv0\pmod{2^d},\\
   0,&r\not\equiv0\pmod{2^d}.
  \end{cases}
  \]
  Here \(r/2^d\) denotes the residue modulo \(2^{n-d}\), including the single residue when \(n=d\).

## Assumptions and scope

The variables range over complete residue rings, with repetition and zero permitted. There is no restriction on the valuations of the inputs. This result gives representation counts, not just the set of targets with a representation. The exponent is \(2^t\), \(t\ge2\); no claim is made for other exponents, other primes, or integer equality.

## Proof

For \(n\ge h\), the group of units modulo \(2^n\) is \(\langle-1\rangle\times\langle5\rangle\), with \(5\) of order \(2^{n-2}\). Raising to \(d=2^t\) kills the sign, and the cyclic factor contributes \(2^t\) elements to the kernel. The powers of \(5\) raised to \(d\) are congruent to \(1\) modulo \(2^h\): the valuation of \(5^{2^t}-1\) is \(t+2\), by repeated squaring, starting with \(v_2(5-1)=2\) and using \(5^{2^j}+1\equiv2\pmod 4\). The image size is \(2^{n-h}\), so the image is the entire subgroup congruent to \(1\) modulo \(2^h\), and each element has \(2^{t+1}\) preimages. Reduction from modulus \(2^h\) implies that odd powers are all \(1\) at every smaller modulus.

Since \(h\le d\), every even \(d\)-th power is \(0\) modulo \(2^h\). For \(2\le n<h\), the parity patterns even/even, mixed, and odd/odd therefore contribute \(q^2/4,q^2/2,q^2/4\) pairs to distinct targets. For \(n=1\), the even/even and odd/odd targets coincide, giving two pairs for each target. The modulus \(1\) has just one pair.

For \(n\ge h\), the three parity patterns land in the disjoint classes \(0,1,2\) modulo \(2^h\). For a mixed target \(r\equiv1\), fix any even input; subtracting its power leaves a unit target with \(2^{t+1}\) odd roots. There are \(q/2\) choices of even input and two possible orders. For \(r\equiv2\), fix any of the \(q/2\) choices of odd first input; subtracting its power again leaves exactly \(2^{t+1}\) odd roots. This yields the two asserted counts.

If both inputs are even and \(h\le n<d\), all \(q^2/4\) pairs give zero. If \(n\ge d\), write \(x=2u\), \(y=2v\), with \(u,v\) modulo \(2^{n-1}\). This branch requires \(2^d\mid r\), and in that case the reduced congruence is \(u^d+v^d\equiv r/2^d\pmod{2^{n-d}}\). Each member of a reduced pair has \(2^{d-1}\) lifts. This gives the factor \(2^{2(d-1)}\), including at \(n=d\), and strictly reduces \(n\).

## Verification

The supplied `verify.py` forms an ordered-pair histogram by cyclic convolution of single-power multiplicities, and compares every target against the recursion. Its 44 cases are \(t=2,3\), \(0\le n\le11\), and \(t=4,5\), \(0\le n\le9\). The finite check is not a substitute for the proof.

## Relationship to prior work and limitations

*Exact subthreshold dyadic images of even-power sums* [1] proves the finite support and the dyadic image and its Haar measure for \(k\ge6\) even and subthreshold summand counts. At \(k=2^t\), with two summands and \(t\ge3\), it gives the image \(\{0\}\cup\bigcup_{j\ge0}2^{dj}((1+2^h\mathbb Z_2)\cup(2+2^h\mathbb Z_2))\) and the measure \(2^{d-t-1}/(2^d-1)\). Its proof also uses the disjoint parity branches and all-even scaling for support. No image or Haar-measure novelty is asserted here. The fiber law requires the multiplicities within each of those classes and the lift factor for pairs, neither of which is given by the support cardinalities. A later dated record [2] gives an equivalent fiber law on the present range as part of a theorem for all even \(k\ge4\).

The odd-unit power map is classical; for fourth powers its surjectivity onto \(1+16\mathbb Z_2\) also appears in the local argument of Brüdern and Wooley [3, Lemmas 7.3–7.4]. The distinct claim here is the complete all-target ordered distribution and its exact recursion, not the unit-power lemma or the zero-target count alone. Ramanujam's p-adic Waring work [4] and Wang's work on Poincaré series of diagonal forms [5] are relevant; earlier equivalent or implicit all-target formulas in that literature have not been ruled out.

## References

1. *Exact subthreshold dyadic images of even-power sums*, 2026-10-13, [record 43f52adb715f](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-exact-subthreshold-dyadic-images-of-even-power-sums--43f52adb715f).
2. *Full 2-adic representation laws for sums of two even powers*, 2026-11-02, [record 4a65caa0042e](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-full-2-adic-representation-laws-for-sums-of-two-even-powers--4a65caa0042e).
3. J. Brüdern and T. D. Wooley, *Pairs of diagonal quartic forms: the non-singular Hasse principle*, Q. J. Math. 74 (2023), 101–128, [arXiv:2110.04349](https://arxiv.org/abs/2110.04349), [DOI 10.1093/qmath/haac019](https://doi.org/10.1093/qmath/haac019).
4. C. P. Ramanujam, *Sums of m-th powers in p-adic rings*, Mathematika 10 (1963), 137–146, [DOI 10.1112/S002557930000406X](https://doi.org/10.1112/S002557930000406X).
5. J. Wang, *On the Poincaré series for diagonal forms*, Proc. Amer. Math. Soc. 116 (1992), 607–611, [DOI 10.2307/2159425](https://doi.org/10.2307/2159425).
