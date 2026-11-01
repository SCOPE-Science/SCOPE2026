# Universal four-per-degree phase retrieval on two parallel lines

## Finding

Let \(d\geq1\) be an integer and let \(L_0,L_1\) be any two distinct parallel lines in the complex plane. Choose **any** \(2d+1\) pairwise distinct points on \(L_0\) and **any** \(2d-1\) pairwise distinct points on \(L_1\). For all complex polynomials \(P,Q\) of degree at most \(d\), equality of their moduli at these \(4d\) sampling points implies
\[
P=cQ\quad\text{for some }c\in\mathbb C,\ |c|=1.
\]
This includes the zero polynomial and all lower-degree cases, and does not require regular spacing, generic positions, or adaptation of sampling points to the unknown polynomial.

More constructively, the same \(4d\) squared-modulus measurements recover the two complete real-polynomial intensity traces along the lines by **linear interpolation**. The sampling map is an isomorphism on the natural real vector space of formal trace pairs with matching two highest coefficients; this ambient space has dimension exactly \(4d\). Therefore \(4d\) is optimal for linear recovery of arbitrary members of this *ambient trace-pair space*. No optimality claim is made for nonlinear phase retrieval from actual polynomial intensities.

## Assumptions and scope

An orientation-preserving affine change of variable reduces the lines to \(L_j=\{x+ih_j:x\in\mathbb R\}\), where \(h_0,h_1\in\mathbb R\) and \(h_0\ne h_1\). Write the sample sets as
\[
\{x_k+ih_0:0\le k\le2d\},\qquad
\{y_k+ih_1:0\le k\le2d-2\},
\]
where the real \(x_k\)'s are pairwise distinct and the real \(y_k\)'s are pairwise distinct. A polynomial may have degree strictly smaller than \(d\). The observations are exact moduli (or, equivalently, squared moduli); stability under noise is not asserted.

For \(P(z)=\sum_{k=0}^{d}a_kz^k\), set \(a_{-1}=0\) and define the line-intensity polynomial
\[
I_h^P(x)=|P(x+ih)|^2\quad (x\in\mathbb R).
\]
It is a real polynomial of degree at most \(2d\), and its two highest coefficients are
\[
[x^{2d}]I_h^P=|a_d|^2,\qquad
[x^{2d-1}]I_h^P=2\operatorname{Re}(a_d\overline{a_{d-1}}),
\]
independently of \(h\).

## Proof

**1. Both line traces are determined.** Suppose \(P,Q\) have matching observations. On the first line, the difference \(I_{h_0}^P-I_{h_0}^Q\) has degree at most \(2d\) and vanishes at \(2d+1\) distinct real abscissae. Therefore it vanishes identically. Its two leading coefficients vanish, and the displayed leading-coefficient identities show that the difference \(I_{h_1}^P-I_{h_1}^Q\) on the second line has degree at most \(2d-2\). It vanishes at \(2d-1\) distinct abscissae, so it too vanishes identically. Thus \(P\) and \(Q\) have equal moduli along **both entire lines**.

**2. A rational function unimodular on two distinct parallel lines is constant.** If one of \(P,Q\) is zero, the first-line polynomial identity forces the other to vanish identically, proving the assertion. Otherwise let \(R=P/Q\), a nonzero rational function. For any real \(h\) define the reflected rational function
\[
R_h^{\#}(z)=\overline{R(\bar z+2ih)}.
\]
On the line of height \(h\), wherever \(R\) is defined, the identity \(|R|=1\) gives \(R(z)R_h^{\#}(z)=1\). Since two rational functions agreeing at infinitely many points agree identically, this holds as a rational-function identity for \(h=h_0,h_1\). Consequently \(R_{h_0}^{\#}=R_{h_1}^{\#}\) and therefore
\[
R(z+2i(h_1-h_0))=R(z)
\]
identically. A nonconstant rational function has no nonzero period: a rational function with a finite pole would acquire infinitely many poles; a nonconstant polynomial has no nonzero period by comparing its leading terms. Hence \(R=c\) is constant. Its modulus is one by either line identity. Thus \(P=cQ\).

**3. Explicit interpolation and the ambient dimension.** From the \(2d+1\) values \(I_{h_0}^P(x_k)\), ordinary Lagrange interpolation determines the real polynomial \(I_{h_0}^P\). Its top two coefficients determine those of \(I_{h_1}^P\). Subtract their terms from the second trace: its residual has degree at most \(2d-2\) and is determined by its \(2d-1\) values at \(y_k\). Thus both traces are explicitly recovered. They determine \(P\) up to phase: factor the polynomial identity \(I_{h_0}^P(z-ih_0)=P(z)\overline{P(\bar z+2ih_0)}\), enumerate its finitely many possible degree-bounded reflected-factor allocations (modulo common phase), and retain the candidate matching the recovered second trace; step 2 makes it unique. In particular no information from other curves is required.

Formally, let \(\mathcal W_d\) be the real vector space of pairs of real polynomials of degree at most \(2d\) with identical coefficients at degrees \(2d\) and \(2d-1\). Its real dimension is \(4d\), and the preceding interpolation argument proves that evaluation at the prescribed \(4d\) points gives a linear isomorphism from \(\mathcal W_d\) to \(\mathbb R^{4d}\). Fewer than \(4d\) real linear measurements cannot be injective on this whole ambient space. Actual intensity trace pairs form a nonlinear subset of \(\mathcal W_d\); this ambient statement does **not** imply a global lower bound on the number of phaseless samples.

## Verification

The proof of injectivity is exact for every integer \(d\ge1\), every pair of distinct parallel lines, and arbitrary distinct nodes on each line. As supplementary finite regression checks, run `python3 checker.py` with Python's standard library. It verifies exact Gaussian-integer expansions of line-intensity coefficients, the height-independence of the top two coefficients, and exact rational Lagrange reconstruction of both traces in 390 deterministic trials across degrees 1 through 6, including zero and lower-degree polynomials. These finite tests do not replace the reflection-and-periodicity proof.

## Relationship to prior work

Przybyłek and Siedlecki (arXiv:1907.09371, Theorem 4.2) give a nonadaptive polynomial-time complex-polynomial phase-retrieval algorithm using \((2d+1)^2\) radial/angular measurements. The present theorem uses \(4d\) **value-only** samples with arbitrary placement along two specified parallel lines and an exact two-trace interpolation mechanism. Bodmann and Hammen (arXiv:1302.5487) give \(4d\)-scale low-redundancy frame constructions; Philipp (arXiv:1403.4769, Theorem 1.1) gives \(4d\) measurements for degree at most \(d\) using values and **derivatives** on a circle. Neither measurement design is a two-parallel-line value-only theorem with arbitrary nodes.

Liehr (arXiv:2308.05722, Theorem 1.1) classifies unions of horizontal lines for unrestricted entire-function phase retrieval and shows that two parallel lines do **not** suffice for that broad class. Chalendar and Partington (arXiv:2403.16255, Section 2.3 and Theorem 2.13) study uniqueness for half-plane Hardy functions from continuous entire-line measurements, and their Section 2.2 provides finite sampling criteria for certain Blaschke products on circles. Those results motivate the polynomial distinction but do not state this finite universal parallel-line construction. The present finite-dimensional positive result is consistent with the negative unrestricted-entire-function result.

## Limitations

The result concerns exact noiseless recovery of degree-bounded **polynomials**, not general entire functions, Hardy-space elements, or unknown degree bounds. It supplies an existence-level exact reconstruction procedure through polynomial factorization, not numerical conditioning estimates or a polynomial bit-complexity guarantee for arbitrary real nodes. The number \(4d\) is the exact dimension of the ambient linear trace-interpolation space; it has **not** been proved minimal for the nonlinear polynomial phase-retrieval problem. Related general structured-frame theorems may have unrecognized implications for this sampling geometry; historical priority has not been independently established.

## References

- M. R. Przybyłek and P. Siedlecki, *A note on the complexity of a phaseless polynomial interpolation*, arXiv:1907.09371 (first public 2019-07-22), especially Section 4 and Theorem 4.2. https://arxiv.org/abs/1907.09371
- B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (first public 2013-02-22), especially Section 2. https://arxiv.org/abs/1302.5487
- F. Philipp, *Phase Retrieval from 4N-4 Measurements*, arXiv:1403.4769 (first public 2014-03-19), especially Theorem 1.1. https://arxiv.org/abs/1403.4769
- L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722 (first public 2023-08-10), Theorem 1.1. https://arxiv.org/abs/2308.05722
- I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first public 2024-03-24), Section 2.3 and Theorem 2.13. https://arxiv.org/html/2403.16255v3
