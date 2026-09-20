# Sharp threshold-2 Lévy inflation under pairwise-independent Rademacher increments

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Let \(X_1,\ldots,X_n\) be pairwise independent symmetric Rademacher random variables,
\[
\Pr(X_i=1)=\Pr(X_i=-1)=\tfrac12,
\qquad S_k=\sum_{i=1}^k X_i.
\]
For odd \(n\), define the threshold-2 maximal-to-terminal tail ratio
\[
R(X_1,\ldots,X_n)
=
\frac{\Pr(\max_{1\le k\le n}|S_k|\ge2)}
{\Pr(|S_n|\ge2)}.
\]
Then
\[
\boxed{R(X_1,\ldots,X_n)\le n+1.} \tag{1}
\]
Moreover, whenever
\[
n=2^m-1,\qquad m\ge4,
\]
the bound is attained. Hence
\[
\boxed{
\sup R(X_1,\ldots,X_n)=n+1
\quad\text{for } n=2^m-1,\ m\ge4.
} \tag{2}
\]

Thus the classical dimension-free Lévy comparison for mutually independent symmetric increments has no dimension-free analogue under pairwise independence, even for identically distributed \(\{\pm1\}\)-valued increments. At the fixed threshold \(2\), the optimal inflation factor is already linear in \(n\) along the infinite family \(n=2^m-1\).

For comparison, mutual independence and symmetry give the classical Lévy inequality
\[
\Pr\!\left(\max_{k\le n}|S_k|\ge t\right)
\le 2\Pr(|S_n|\ge t).
\]

## Proof of the universal upper bound

Pairwise independence and centering imply
\[
\mathbb E S_n^2
=
\sum_{i=1}^n\mathbb E X_i^2
=n. \tag{3}
\]
Because \(n\) is odd, \(S_n\) is odd. Put
\[
p=\Pr(|S_n|\ge2).
\]
On the complementary event one has \(|S_n|=1\), while always \(|S_n|\le n\). Therefore
\[
n=\mathbb E S_n^2
\le (1-p)\cdot1+p\,n^2,
\]
so
\[
p\ge\frac{n-1}{n^2-1}=\frac1{n+1}. \tag{4}
\]
The numerator in \(R\) is at most one. Combining this with (4) proves (1).

The parity analogue for even \(n\) is also immediate: since \(|S_n|<2\) then means \(S_n=0\), (3) gives \(\Pr(|S_n|\ge2)\ge1/n\), and therefore the same threshold-2 ratio is at most \(n\). No sharpness claim for the even case is made here.

## Sharp construction at \(n=2^m-1\)

Let \(V=\mathbb F_2^m\), with standard basis \(e_1,\ldots,e_m\), and let \(U\) be uniform on \(V\). For every nonzero \(v\in V\), define the character
\[
\chi_v(U)=(-1)^{\langle v,U\rangle}.
\]
Any two distinct nonzero vectors of \(V\) are linearly independent over \(\mathbb F_2\), so their two characters are independent symmetric Rademachers. Thus any ordering of the \(2^m-1\) nonzero characters gives a pairwise-independent symmetric Rademacher sequence.

Choose the first six vectors in the order
\[
\boxed{
e_1,
\ e_2,
\ e_1+e_2,
\ e_3,
\ e_4,
\ e_3+e_4
} \tag{5}
\]
and append all remaining nonzero vectors in any order. This requires only \(m\ge4\).

We first show that every sample point reaches absolute partial sum at least \(2\) within those first six increments. Split (5) into three consecutive pairs and write their pair-differences as
\[
d_1=e_1+e_2,
\qquad
d_2=e_1+e_2+e_3,
\qquad
d_3=e_3.
\]
They satisfy
\[
d_1+d_2+d_3=0. \tag{6}
\]
Suppose, to the contrary, that the first six partial sums all remain in \(\{-1,0,1\}\). Starting from zero, each consecutive two-step block must then consist of opposite signs; otherwise the second increment in that block reaches \(2\) or \(-2\). Hence for each \(j=1,2,3\),
\[
\chi_{d_j}(U)=-1,
\qquad\text{equivalently}\qquad
\langle d_j,U\rangle=1.
\]
Adding the three equations in \(\mathbb F_2\) contradicts (6), because the left side is zero and the right side is one. Consequently
\[
\Pr\!\left(\max_{k\le n}|S_k|\ge2\right)=1. \tag{7}
\]

For the terminal sum, character orthogonality gives
\[
\sum_{v\in V}(-1)^{\langle v,U\rangle}
=
\begin{cases}
2^m,&U=0,\\
0,&U\ne0.
\end{cases}
\]
After removing the zero character,
\[
S_n=
\begin{cases}
n,&U=0,\\
-1,&U\ne0.
\end{cases} \tag{8}
\]
Therefore
\[
\Pr(|S_n|\ge2)=2^{-m}=\frac1{n+1}. \tag{9}
\]
Equations (7) and (9) give \(R=n+1\), matching the universal upper bound (1) and proving (2).

## Context and originality check

Lévy's classical maximal inequality compares the maximum partial-sum tail with the terminal-sum tail by a constant factor under mutual independence and symmetry. The Encyclopedia of Mathematics entry records the usual two-sided bound with constant \(2\) and traces it to Lévy's 1937 monograph.

The limited-independence literature already makes clear that maximal inequalities can fail badly. Révész and Wschebor studied partial sums of the Walsh system, explicitly noting that Walsh functions are pairwise independent but not mutually independent and deriving detailed partial-sum behavior. More recently, Thành's 2023 paper on weak laws for maximal partial sums states that the Kolmogorov-type maximal inequality used under stronger dependence assumptions does not hold for pairwise-independent random variables, and develops a method that avoids it.

The finite-field character family used above is itself standard. For example, Tao's *Topics in Random Matrix Theory* uses the same \(2^m-1\) nonzero characters to show sharp heavy tails for a terminal sum under pairwise independence: the total sum equals \((n+1)1_{\{U=0\}}-1\).

The contribution here is the exact maximal-versus-terminal optimization at threshold \(2\): the elementary second-moment/parity argument gives the universal factor \(n+1\), while the six-character prefix (5) forces the maximal event with probability one without changing the extremal terminal distribution, so the factor is attained for every \(n=2^m-1\), \(m\ge4\). Targeted searches under “pairwise independent Lévy inequality”, “Ottaviani pairwise independent”, “pairwise independent Rademacher maximal partial sums”, “Hadamard matrix Lévy inequality”, and maximal/final-sum terminology did not locate this sharp factor or this six-step construction. Originality is therefore claimed only **to the best of our knowledge**.

A residual risk is that the same extremal ratio may be implicit in older Walsh/orthogonal-system literature under different language. Révész--Wschebor (1964) is the closest located source: it studies the same Walsh characters and their partial sums, but the inspected theorem concerns natural Walsh ordering and does not state the sharp threshold-2 Lévy ratio (2). Hoffmann-Jørgensen's work on “perfect independence” extends Lévy/Ottaviani inequalities to weaker formulations appropriate to non-measurable random elements; the inspected description concerns notions designed to retain the relevant stochastic inequalities, not mere pairwise independence, and therefore does not cover the counterexample above.

## Verification

`artifacts/verify.py` exhaustively enumerates all seeds for \(4\le m\le9\). It checks symmetric Rademacher marginals, every pairwise \(2\times2\) joint table, the probability-one maximal event from the prescribed six-vector prefix, and the exact terminal distribution. `artifacts/verification_output.txt` records the resulting exact counts.

The computational check supports the finite construction but is not used in place of the proof.

## Limitations

- The exact sharpness statement is for the fixed threshold \(2\) and the subsequence of lengths \(n=2^m-1\), \(m\ge4\). It does not determine the optimal ratio for every \(n\) or every threshold.
- The increments are pairwise independent but highly dependent jointly; no mixing, martingale-difference, conditional-independence, or higher-wise-independence assumption is imposed.
- The theorem is scalar and Rademacher-valued. It does not identify best constants for general symmetric marginals or Banach-space-valued sums.
- Originality is to the best of our knowledge; an equivalent older formulation in Walsh-function, orthogonal-system, or maximal-inequality literature may exist.

## References

1. Encyclopedia of Mathematics, “Lévy inequality”: https://encyclopediaofmath.org/wiki/L%C3%A9vy_inequality
2. P. Révész and M. Wschebor, “On the statistical properties of the Walsh functions,” *A Magyar Tudományos Akadémia Matematikai Kutató Intézetének Közleményei* 9 (1964), 543–554: https://real.mtak.hu/189835/1/cut_MATKUTINT_1964_3_pp543_-_554.pdf
3. Lê Vǎn Thành, “On weak laws of large numbers for maximal partial sums of pairwise independent random variables,” *Comptes Rendus Mathématique* 361 (2023), 577–585, DOI 10.5802/crmath.387: https://doi.org/10.5802/crmath.387
4. Terence Tao, *Topics in Random Matrix Theory*, Graduate Studies in Mathematics 132, AMS (2012), online draft: https://terrytao.wordpress.com/wp-content/uploads/2011/08/matrix-book.pdf
5. J. Hoffmann-Jørgensen, “Stochastic inequalities and perfect independence,” in *High Dimensional Probability III* (2003), 3–34, DOI 10.1007/978-3-0348-8059-6_1: https://doi.org/10.1007/978-3-0348-8059-6_1
