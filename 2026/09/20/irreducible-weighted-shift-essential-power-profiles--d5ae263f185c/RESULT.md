# Exact norm and essential-norm power profiles for irreducible weighted shifts

## Statement

Let \((a_n)_{n\ge 0}\) be a strictly positive real sequence with \(a_0=1\). The following are equivalent.

1. \(a_{m+n}\le a_m a_n\) for all \(m,n\ge 0\).
2. There is an irreducible unilateral weighted shift \(W\) on \(\ell_2(\mathbb N_0)\) such that
   \[
   \|W^n\|=\|W^n\|_e=a_n\qquad(n\ge 0),
   \]
   where \(\|\cdot\|_e\) denotes essential norm.

Thus every strictly positive submultiplicative sequence is simultaneously the operator-norm and Calkin-norm power profile of a single irreducible weighted shift.

A useful consequence concerns exact rates in the spectral-radius formula. If \((\rho_n)_{n\ge1}\) is any strictly positive nonincreasing sequence with \(\rho_n\to r\ge0\), then there is an irreducible unilateral weighted shift \(W\) such that
\[
\|W^n\|^{1/n}=\|W^n\|_e^{1/n}=\rho_n\qquad(n\ge1).
\]
Hence both the spectral radius and the essential spectral radius of \(W\) equal \(r\). In particular, when \(r=0\), one obtains an injective irreducible quasinilpotent Riesz operator for which no positive power is compact, while the convergence to zero in both spectral-radius formulas follows the prescribed sequence \((\rho_n)\) exactly.

## Proof

### Necessity

For every bounded operator,
\[
\|W^{m+n}\|\le \|W^m\|\,\|W^n\|,
\]
so any power-norm profile is submultiplicative. Also \(a_0=\|I\|=1\).

### A recurrent version of the Wallen construction

Assume now that \((a_n)\) is strictly positive and submultiplicative. Define
\[
\beta_k=\frac{a_{k+1}}{a_k}\qquad(k\ge0).
\]
Submultiplicativity gives \(\beta_k\le a_1\). Moreover, for every \(j,n\ge0\),
\[
\beta_j\beta_{j+1}\cdots\beta_{j+n-1}
=\frac{a_{j+n}}{a_j}
\le a_n.
\]
For \(m\ge1\), let
\[
B_m=(\beta_0,\beta_1,\ldots,\beta_{m-1}).
\]
We build an infinite positive weight sequence by concatenating longer and longer copies of these prefixes,
\[
B_1,\delta_1,B_2,\delta_2,B_3,\delta_3,\ldots,
\]
with the bridge weights \(\delta_m>0\) chosen inductively.

Suppose a finite initial word has already been built so that every contiguous product of length \(n\) is at most \(a_n\). Append \(\delta_m B_{m+1}\). Products lying entirely in the old word already satisfy the required bound, and products lying entirely in \(B_{m+1}\) satisfy it by the displayed ratio identity. Every genuinely new crossing product contains \(\delta_m\) exactly once and has the form
\[
C\,\delta_m\,D,
\]
where \(C,D>0\) are fixed products from the two adjacent finite words. There are only finitely many such constraints at this stage, and every target \(a_n\) is positive. Hence \(\delta_m\) can be chosen positive and sufficiently small that all crossing products satisfy \(C\delta_mD\le a_n\); we also impose \(\delta_m\le a_1\). Induction produces a bounded positive weight sequence \((w_j)_{j\ge0}\), with \(0<w_j\le a_1\), such that every contiguous product of \(n\) weights is at most \(a_n\).

Let \(W\) be the unilateral weighted shift
\[
We_j=w_j e_{j+1}.
\]
For a unilateral weighted shift,
\[
\|W^n\|=\sup_{j\ge0} w_jw_{j+1}\cdots w_{j+n-1}.
\]
The construction gives the upper bound \(\|W^n\|\le a_n\). On the other hand, every block \(B_m\) with \(m\ge n\) begins with
\[
\beta_0\beta_1\cdots\beta_{n-1}=a_n.
\]
Therefore \(\|W^n\|=a_n\).

### Exact essential norms

Fix \(n\ge1\), and let \(s_m\) denote the initial index of the block \(B_m\). For every \(m\ge n\),
\[
\|W^n e_{s_m}\|=a_n.
\]
The vectors \((e_{s_m})_{m\ge n}\) form an orthonormal, hence weakly null, sequence. If \(K\) is compact, then \(Ke_{s_m}\to0\) in norm, so
\[
\|W^n-K\|
\ge \limsup_{m\to\infty}\|(W^n-K)e_{s_m}\|
=a_n.
\]
Taking the infimum over compact \(K\) yields \(\|W^n\|_e\ge a_n\). Since always \(\|W^n\|_e\le\|W^n\|=a_n\), equality follows.

### Irreducibility

All weights are positive. Hence
\[
\ker W^*=\operatorname{span}\{e_0\}.
\]
If \(P\) is the orthogonal projection onto a reducing subspace for \(W\), then \(P\) commutes with both \(W\) and \(W^*\). Thus \(Pe_0\in\ker W^*\), and because \(P\) is a projection, \(Pe_0\) is either \(0\) or \(e_0\). Since every \(e_n\) is a nonzero scalar multiple of \(W^n e_0\), the first case forces \(P=0\) and the second forces \(P=I\). Therefore \(W\) is irreducible.

This completes the equivalence.

### Exact spectral-radius and essential-spectral-radius rates

Let \((\rho_n)_{n\ge1}\) be strictly positive and nonincreasing, and put \(a_0=1\), \(a_n=\rho_n^n\) for \(n\ge1\). Then
\[
\rho_{m+n}^{m+n}
\le \rho_m^m\rho_n^n,
\]
because \(\rho_{m+n}\le\rho_m\) and \(\rho_{m+n}\le\rho_n\). Hence \((a_n)\) is submultiplicative, and the theorem gives
\[
\|W^n\|^{1/n}=\|W^n\|_e^{1/n}=\rho_n.
\]
Applying the spectral-radius formula in \(\mathcal B(\ell_2)\) and in the Calkin algebra gives
\[
r(W)=r_e(W)=\lim_{n\to\infty}\rho_n=r.
\]
When \(r=0\), the operator is quasinilpotent and its essential spectrum is \(\{0\}\), so it is Riesz. Because \(a_n>0\) for every \(n\), \(\|W^n\|_e>0\) for every \(n\), and no positive power of \(W\) is compact.

## Context

The operator-norm half of the realization problem is classical. Halmos's *A Hilbert Space Problem Book*, Solution 92, records a theorem due to L. J. Wallen: a nonnegative sequence with \(p_0=1\) is a sequence of power norms of a bounded operator exactly when it is submultiplicative, and the realizing operator may be taken to be a weighted shift. The ratio weights \(p_{n+1}/p_n\) are the starting point of the construction above.

The additional conclusion here is that, for strictly positive profiles, the same sequence can be realized simultaneously as the ordinary and essential power norms while keeping the realizing shift irreducible. Repeating increasingly long Wallen prefixes infinitely far out forces every prescribed norming product to recur on a weakly null sequence; arbitrarily small positive bridges preserve all upper bounds without introducing zero weights.

Young observed that in a general Banach algebra the spectral-radius formula may approach its limit arbitrarily slowly. The corollary above gives an exact realization of every positive nonincreasing rate, simultaneously for the ordinary and essential spectral-radius formulas, inside the narrow class of irreducible unilateral weighted shifts. For rates tending to zero it gives irreducible Riesz shifts that are not power compact.

## Limitations

The ordinary power-norm characterization is not new; it is the classical Wallen theorem recorded by Halmos. The originality claim here concerns the simultaneous equality \(\|W^n\|=\|W^n\|_e=a_n\) with an irreducible unilateral weighted shift, together with the exact-rate Riesz consequence.

Targeted literature searches using combinations of power norms, essential norms, Calkin norms, submultiplicative sequences, irreducible weighted shifts, prescribed spectral-radius rates and Riesz weighted shifts did not locate this strengthening. Shields's 1974 survey on weighted shifts was identified as a particularly relevant classical source but was not exhaustively inspected page by page, and Wallen's original source was not identified beyond Halmos's explicit attribution. Because the bridge construction is elementary once Wallen's ratio weights are known, an equivalent observation may exist under different weighted-shift or essential-spectrum terminology. Originality is therefore asserted only to the best of our knowledge.

No computational verification is required; the proof is explicit and uses only weighted-shift power norms, compactness on weakly null orthonormal sequences, and the Calkin spectral-radius formula.

## References

1. P. R. Halmos, *A Hilbert Space Problem Book*, 2nd ed., Graduate Texts in Mathematics 19, Springer, 1982, Solution 92. https://doi.org/10.1007/978-1-4684-9330-6
2. A. L. Shields, *Weighted shift operators and analytic function theory*, in *Topics in Operator Theory*, Mathematical Surveys 13, American Mathematical Society, 1974, 49–128. https://doi.org/10.1090/surv/013/02
3. N. J. Young, *Norm and spectral radius for algebraic elements of a Banach algebra*, Math. Proc. Cambridge Philos. Soc. **88** (1980), 129–133. https://doi.org/10.1017/S0305004100057406
4. P. S. Bourdon and J. H. Shapiro, *Riesz composition operators*, Pacific J. Math. **181** (1997), 231–246. https://msp.org/pjm/1997/181-2/pjm-v181-n2-p02-p.pdf
