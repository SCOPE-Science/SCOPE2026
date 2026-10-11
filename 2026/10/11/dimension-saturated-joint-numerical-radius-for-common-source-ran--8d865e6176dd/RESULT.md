# Dimension-saturated joint numerical radius for common-source rank-one tuples

## Finding

For every integer \(m\ge2\), integer \(k\ge1\), and real or complex \(m\)-dimensional Hilbert space \(H\), let \(v\in H\) be a unit vector and \(u_1,\ldots,u_k\in H\) not all zero. Define \(T_i x=\langle x,v\rangle u_i\), using the convention that the inner product is linear in the first variable. Put \(q=\min\{k,m-1\}\) and

\[
 W=\sup_{\|x\|=1}\left(\sum_{i=1}^k|\langle T_i x,x\rangle|^2\right)^{1/2},\qquad
 N=\sup_{\|x\|=1}\left(\sum_{i=1}^k\|T_i x\|^2\right)^{1/2}.
\]

The **optimal common-source ratio** is exactly

\[
 \boxed{\inf_{\sum_i\|u_i\|^2>0}\frac{W}{N}=\frac{1}{2\sqrt{\min\{k,m-1\}}}.}
\]

Equality holds if and only if \(u_i\perp v\) for every \(i\), and the nonzero singular values of the synthesis operator \(U:\mathbb F^k\to v^\perp\), \(Uc=\sum_i c_i u_i\), are all equal and their number is exactly \(q\). Thus if \(k\le m-1\), the output vectors form a mutually orthogonal equal-norm family; if \(k\ge m-1\), they form a tight frame of the entire \(v^\perp\) (zero vectors permitted). Every possible pair of dimensions admits an equality tuple. In particular the sharp value **stops decreasing with \(k\)** once \(k\ge m-1\).

There is also an exact spectral deficit in the orthogonal-source case. Write \(u_i=a_i v+b_i\) with \(b_i\perp v\), \(a_i\in\mathbb F\), let \(S:\mathbb F^k\to v^\perp\) have columns \(b_i\), and pad its singular values \(s_1\ge\cdots\ge s_q\ge0\) with zeros. Then

\[
 4W^2-\frac{N^2}{q}\ \ge\
 \frac{q-1}{q}\sum_i|a_i|^2+\frac1q\sum_{j=1}^{q}(s_1^2-s_j^2).
\]

When every \(a_i=0\) this inequality is an identity. For \(q\ge2\), normalized tuples with \(N=1\) and \(W^2\le1/(4q)+\varepsilon\) obey \(\sum_i|a_i|^2\le4q\varepsilon/(q-1)\) and \(\sum_{j=1}^q(s_1^2-s_j^2)\le4q\varepsilon\).

## Assumptions and scope

The scalar field \(\mathbb F\) is exactly \(\mathbb R\) or \(\mathbb C\). The dimension \(m\) is finite and at least two. The tuple has length \(k\ge1\) and every member is of rank at most one and has the same source vector \(v\). Some \(u_i\) may vanish, but not all. The norms \(N\) and \(W\) are the Euclidean joint operator norm and joint numerical radius, respectively. No claim is made about unrestricted operator tuples, and the complex Hilbert numerical-index result for \(k<m\) is a pre-existing theorem rather than a new assertion.

## Proof

**1. Joint norm and a rank-one reduction.** Since \(T_i x=\langle x,v\rangle u_i\),

\[
 N^2=\sum_i\|u_i\|^2=\sum_i|a_i|^2+\|S\|_{\mathrm{HS}}^2.
\]

For clarity, the ordinary numerical radius of the rank-one operator \(x\mapsto\langle x,v\rangle u\) with \(\|v\|=1\) is

\[
 \frac12\big(\|u\|+|\langle u,v\rangle|\big).
\]

Indeed write \(u=\alpha v+w\) with \(w\perp v\). On the two-dimensional span of \(v,w\), optimizing the phase of a test vector reduces the numerical quadratic form to the largest eigenvalue of the real symmetric matrix with entries \(|\alpha|,\|w\|/2;\|w\|/2,0\). Its largest eigenvalue is \((|\alpha|+\sqrt{|\alpha|^2+\|w\|^2})/2\), and vectors outside this span cannot improve the supremum. Consequently, if \(V:\mathbb F^k\to H\) has columns \(u_i\), duality of the Euclidean coefficient norm also gives the exact auxiliary formula

\[
 W=\frac12\max_{\|c\|_2=1}\big(\|Vc\|+|\langle Vc,v\rangle|\big).
\]

**2. Spectral lower bound.** Let \(A=(\sum_i|a_i|^2)^{1/2}\) and \(s_1=\|S\|\). Choose a unit \(y\in v^\perp\) with \(\|S^*y\|=s_1\). This exists in finite dimensions, even when \(S=0\). Test the two unit vectors \((v+y)/\sqrt2\), \((v-y)/\sqrt2\). Their squared joint numerical values have average exactly \((A^2+s_1^2)/4\); hence

\[
 4W^2\ge A^2+s_1^2.
\]

In the complex case the same two vectors suffice, since adding and subtracting cancels the complex cross term in the squared norm. The rank of \(S\) is at most \(q\), so

\[
 \|S\|_{\mathrm{HS}}^2=\sum_{j=1}^{q}s_j^2\le q s_1^2.
\]

Together these give

\[
 4W^2-\frac{N^2}{q}
 \ge \frac{q-1}{q}A^2+\frac1q\sum_{j=1}^{q}(s_1^2-s_j^2)\ge0.
\]

This proves the inequality and its quantitative part without assuming the outputs are perpendicular to the source.

**3. Exact value in the perpendicular class and attainment.** When all \(a_i=0\), every unit \(x=t v+y\) with \(y\perp v\) has

\[
 \left(\sum_i|\langle T_i x,x\rangle|^2\right)^{1/2}
 =|t|\,\|S^*y\|\le |t|\sqrt{1-|t|^2}\,s_1\le s_1/2.
\]

Equality is realized by \(|t|=1/\sqrt2\) and a maximal singular vector, so \(W=s_1/2\). Take \(q\) nonzero output vectors to be mutually orthogonal unit vectors in \(v^\perp\) and all other output vectors zero. Then \(N=\sqrt q\) and \(W=1/2\), attaining the claimed ratio for each \((m,k)\) over both fields. The same calculation proves the claimed spectral-deficit identity when \(a_i=0\).

**4. Classification of equality.** Suppose \(W/N=1/(2\sqrt q)\). The nonnegative terms in the lower bound of step 2 must vanish. If \(q>1\), this forces \(A=0\) and \(s_1=s_2=\cdots=s_q>0\). Conversely those conditions imply equality by step 3.

If \(q=1\), equality still forces \(A=0\), but an extra argument is required. Suppose instead \(A>0\) and choose \(y\in v^\perp\) with \(\|S^*y\|=s_1\). For \(0\le t\le1\), average the squared joint numerical values at \(x_\pm=\sqrt t\,v\pm\sqrt{1-t}\,y\). This gives

\[
 W^2\ge t^2 A^2+t(1-t)s_1^2.
\]

At \(t=1/2\), the right side is \(N^2/4\), because \(q=1\) implies \(\|S\|_{\mathrm{HS}}=s_1\). Its derivative at \(t=1/2\) is \(A^2>0\); some \(t>1/2\) therefore gives \(W^2>N^2/4\), contradiction. Thus \(A=0\). Now \(\|S\|_{\mathrm{HS}}^2=q s_1^2\) is precisely the condition that \(S\) have rank \(q\) and all its nonzero singular values equal. Equivalently \(S^*S=s_1^2 I\) when \(k\le m-1\), or \(SS^*=s_1^2 I\) on \(v^\perp\) when \(k\ge m-1\), proving the orthogonal-family/tight-frame characterization and completing the proof.

## Verification

Run `python3 verify.py` using Python 3 with NumPy. The checker tests all rectangular coordinate-isometry witness shapes with \(2\le m\le8\), \(1\le k\le10\), exact rational one-dimensional boundary and phase-improvement identities, and \(1680\) deterministic random real/complex Gram-matrix inequalities. Expected output:

`VERIFY_OK exact_witness_assertions=210 rank_equalizers=70 nonorthogonality_tests=70 random_gram_tests=1680 analytic_global_proof_required=True`

These are finite stress tests, not verification for arbitrary dimensions; the proof above supplies the universal quantifiers and equality necessity.

## Relationship to prior work

Mal introduced the joint numerical index and proved the sharp complex Hilbert value \(1/(2\sqrt k)\) for \(k<m\) (2023 journal Theorem 3.11(i); initial 2022 preprint). The exhibited operators have the same source vector, with \(k\) orthogonal outputs. The present restricted-family theorem asks what happens to **that exact mechanism** after the ambient perpendicular dimension is exhausted: it gives the sharp saturation at \(m-1\), its full equality geometry, and a spectral defect. The already-known range \(k<m\) is included only for coherent classification, not presented as independently novel. Grover and Singla's joint-radius subdifferential and orthogonality results address a different optimization question and do not provide this common-source dimension threshold. The earlier Drnovšek–Müller work motivates the original sharpness construction; its full text was not available for a conclusive equivalence check.

## Limitations

The claimed minimum is only within rank-at-most-one tuples sharing one source; it is **not** asserted to equal the unrestricted finite-dimensional Hilbert joint numerical index when \(k\ge m\). Vanishing entries in the tuple are permitted. The quantitative deficit is exact when the outputs are perpendicular, but the general nonperpendicular lower estimate need not be equality. Earlier terminology for the same operator tuple, particularly in literature not available in full text, may conceal equivalent results. No independent mathematical audit has been carried out.

## References

1. A. Mal, *On joint numerical radius of operators and joint numerical index of a Banach space*, arXiv:2212.06500v1 (public 2022-12-13), journal version *Operators and Matrices* 17 (2023), 839–856, DOI:10.7153/oam-2023-17-56, https://files.ele-math.com/articles/oam-17-56.pdf. In particular Theorem 3.11 and its proof.
2. P. Grover and S. Singla, *Subdifferential of the joint numerical radius*, arXiv:2201.03055v1 (2022), https://arxiv.org/pdf/2201.03055; Sections 1–3.
3. R. Drnovšek and V. Müller, *On joint numerical radius II*, *Linear and Multilinear Algebra* 62 (2014), 1197–1204, DOI:10.1080/03081087.2013.816303. Full text not examined; the citation and attribution appear in [1].
4. M. S. Moslehian, M. Sattari and K. Shebrawi, *Extensions of Euclidean operator radius inequalities*, *Mathematica Scandinavica* 120 (2017), 129–144, DOI:10.7146/math.scand.a-25509; only accessible abstract and published metadata were inspected.
