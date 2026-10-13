# Presburger images of power sets have sharp polylogarithmic counting growth

## Finding

Let
\[
E=\bigcup_{j=1}^r a_j^{\mathbb N}\subseteq\mathbb Z,
\qquad a_j>1,
\]
and let \(f:\mathbb Z^M\to\mathbb Z\) be Presburger-definable. Then there is a constant \(C=C(E,f)>0\) such that, for every \(H\ge2\),
\[
\boxed{\,|f(E^M)\cap[-H,H]|\le C(1+\log H)^M\,}.
\]

The exponent \(M\) is optimal as a uniform statement. For every \(M\ge1\), choose an integer \(B>M\), put \(E=B^{\mathbb N}\), and take
\[
f(x_1,\ldots,x_M)=x_1+\cdots+x_M.
\]
If \(L=\lfloor\log_B(H/M)\rfloor\), then all sums of \(M\) powers \(B^e\) with \(0\le e\le L\) lie in \([0,H]\). Because \(B>M\), their base-\(B\) expansions have digit multiplicities below \(B\), so distinct multisets of exponents give distinct sums. Hence
\[
|f(E^M)\cap[0,H]|\ge \binom{L+M}{M}=\Theta((\log H)^M).
\]
Thus Schulz's qualitative conclusion that these images have zero natural density can be strengthened to a sharp polylogarithmic counting law.

## Assumptions and scope

The bases \(a_1,\ldots,a_r\) and the function \(f\) are fixed; the implicit constant may depend on them. Natural logarithms are used only for notation: changing the logarithm base changes the constant. The upper bound concerns the number of distinct image values, not the number of preimages.

The result is a quantitative extraction from the argument in Chris Schulz's *Undefinability of multiplication in Presburger arithmetic with sets of powers*. The source proves zero natural density. It does not state the polylogarithmic bound above.

## Proof

It is enough first to treat a fixed linear-exponential sum. Fix nonzero rational numbers \(k_1,\ldots,k_n\) and integers \(a_i>1\), and let
\[
C_n=\left\{c\in\mathbb Z:\ c=k_1a_1^{e_1}+\cdots+k_na_n^{e_n}\text{ for some }e_i\in\mathbb N\right\}.
\]
We prove by induction on \(n\) that
\[
|C_n\cap[-H,H]|=O((1+\log H)^n).
\]
For \(n=1\), this is immediate because \(|k_1|a_1^e\le H\) permits only \(O(1+\log H)\) exponents.

For the induction step, use exactly Schulz's decomposition in Lemma 3.2. Proposition 3.1, a Schlickewei--Schmidt subspace-theorem consequence, splits solutions into \(S_1\cup S_2\).

For \(S_1\), the normalized vector lies in one of finitely many proper rational linear subspaces. On a fixed subspace there is a nonzero relation
\[
d_1k_1a_1^{e_1}+\cdots+d_nk_na_n^{e_n}=0.
\]
Choose \(d_n\ne0\), solve for the last term, and substitute into the equation for \(c\). Schulz obtains
\[
c=\sum_{i<n}k_i' a_i^{e_i}
\]
with fixed rational coefficients \(k_i'\), discarding any zero coefficients. Hence the image of each subspace is contained in a sumset with at most \(n-1\) exponential terms. There are only finitely many subspaces, so the induction hypothesis gives
\[
|\pi(S_1)\cap[-H,H]|=O((1+\log H)^{n-1}).
\]

For \(S_2\), Schulz's proof is already quantitative. If \(|c|\le H\), his height comparison yields
\[
H(x)<(bH)^{4n^2},
\]
where \(b\) clears the denominators of the \(k_i\), and \(H(x)=\max_i a_i^{e_i}\). Therefore each exponent has only \(O(1+\log H)\) possibilities. In the explicit estimate printed in the proof,
\[
|\pi(S_2)\cap[-H,H]|\le O(1)+(5n^2\log_2(bH))^n.
\]
Combining the two parts proves the induction.

Now let \(f:\mathbb Z^M\to\mathbb Z\) be Presburger-definable. As used by Schulz in the proof of Theorem B, Presburger cell decomposition makes \(f\) piecewise affine with rational coefficients on finitely many pieces. On each piece, and for each of the finitely many choices of one base \(a_j\) for each input coordinate, the image is contained in a translate of a fixed linear-exponential sum with at most \(M\) terms. Clearing denominators and translating change only the constant and the scale of \(H\). A finite union therefore gives
\[
|f(E^M)\cap[-H,H]|=O((1+\log H)^M).
\]

For sharpness, take \(B>M\) and \(f(x)=\sum_i x_i\). For exponents in \(\{0,\ldots,L}\}\), the base-\(B\) digit at position \(e\) is exactly the multiplicity of \(e\), which is at most \(M<B\), so there are no carries. Thus exponent multisets are recovered uniquely from the sum. There are \(\binom{L+M}{M}\) such multisets, yielding the matching lower bound.

## Verification

The key upper-bound estimate is visible directly in Schulz's proof: after the height split, the \(S_2\) contribution is bounded by \((5n^2\log_2(bH))^n\). The only additional step is to strengthen the induction hypothesis on the finitely many \(S_1\) subspaces from “density zero” to the corresponding polylogarithmic counting bound; Schulz's substitution reduces the number of exponential terms by at least one, so the quantitative induction closes.

A finite exact replay of the sharpness construction checks \(1\le M\le7\) and \(0\le L\le8\). It verifies that the number of distinct sums is exactly \(\binom{L+M}{M}\) when \(B=M+1\). The bundled verifier reports `VERIFY_OK 126 exact assertions`.

## Relationship to prior work

Schulz proves that every Presburger-definable image \(f(E^M)\) has zero natural density and uses this to establish undefinability of multiplication in expansions by sets of powers. His Lemma 3.2 invokes the Schlickewei--Schmidt subspace theorem and already contains the logarithmic tuple count for the nondegenerate \(S_2\) part. The quantitative statement here comes from propagating that estimate through the same finite-subspace induction and then through the piecewise-affine reduction used in Theorem B.

Raf Cluckers's Presburger cell decomposition supplies the piecewise-affine description of definable functions used by Schulz. The Schlickewei--Schmidt paper supplies the finite-subspace input. Targeted searches for “polylogarithmic,” \(O((\log H)^M)\), “counting function,” and equivalent formulations located the zero-density theorem and adjacent Presburger/powers literature, but not this quantitative bound or its sharpness statement.

## Limitations

The bound is asymptotic and its constant is not made effective here; tracing the explicit subspace theorem and every cell would give very large constants. The result counts distinct image values and does not bound representation multiplicities. For a specific \(f\), the optimal logarithmic exponent can be smaller than \(M\); the sharpness assertion says that \(M\) cannot be lowered uniformly over all Presburger-definable \(M\)-ary functions and all finite unions of power sets.

## References

- Chris Schulz, *Undefinability of multiplication in Presburger arithmetic with sets of powers*, arXiv:2209.11858 (submitted 23 September 2022), *Journal of Symbolic Logic* 90 (2025), 872--886, DOI 10.1017/jsl.2023.71. In particular Lemma 3.2 and Theorem B.
- H. P. Schlickewei and W. P. Schmidt, *The Number of Solutions of Polynomial-Exponential Equations*, *Compositio Mathematica* 120 (2000), 193--225, DOI 10.1023/A:1001719425893.
- Raf Cluckers, *Presburger sets and p-minimal fields*, *Journal of Symbolic Logic* 68 (2003), 153--162, DOI 10.2178/jsl/1045861509.
