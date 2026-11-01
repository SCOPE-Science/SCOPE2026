# Exact projection constant of a higher-codimension obstruction family

## Finding

Let \(V\subset\ell_\infty^5(\mathbb R)\) be spanned by
\[
 u=(1,4/5,1/4,-1/4,-4/5),\qquad
 v=(0,3/5,1,1,3/5).
\]
For every integer \(n\ge3\), set
\[
W_n=V\oplus\operatorname{span}\{e_6\}
 \oplus\bigoplus_{j=1}^{n-3}\operatorname{span}\{e_{2j+5}+e_{2j+6}\}
 \subset\ell_\infty^{2n}(\mathbb R).
\]
Here elements of \(V\) are extended by zero outside their first five coordinates, and all direct sums are coordinate-disjoint. Define the relative projection constant as the infimum of \(\|P\|\) over linear maps \(P:\ell_\infty^{2n}\to W_n\) with \(P|_{W_n}=\mathrm{id}\). **For every integer \(n\ge3\),**
\[
\boxed{\lambda(W_n,\ell_\infty^{2n})=\lambda(W_n)=\frac{845}{659}.}
\]
The second equality is the standard finite-dimensional \(\ell_\infty\)-embedding identity for the absolute projection constant; see the primary reference, equation (1). In particular, the answer is independent of dimension and is attained by an explicit rational projection. This sharpens the previously exhibited norm \(13/10\) projection on the same natural family [1, Proposition 3.4], without modifying the geometric obstruction established there.

## Assumptions and scope

All vector spaces, maps, and norms are **real**. The norm on \(\ell_\infty^d\) is the maximum absolute coordinate; hence the induced norm of a matrix is its maximum absolute row sum. No assumption is made on symmetry, sparsity, or signs of a competing projection. The family \(W_n\) is exactly the coordinate direct-sum obstruction in [1, Proposition 3.2], for every integer \(n\ge3\). This result is about its **minimum projection norm**, not the Banach--Mazur estimate or the universal higher-codimension conjecture of [1].

## Proof

**Step 1: reduction to five coordinates.** Let \(P\) be any projection from \(\ell_\infty^{2n}\) onto \(W_n\). Restricting inputs to the first five coordinates and then retaining the first five output coordinates gives a map \(Q:\ell_\infty^5\to V\) with \(Q|_V=\mathrm{id}\) and \(\|Q\|\le\|P\|\). Therefore
\[
\lambda(W_n,\ell_\infty^{2n})\ge\lambda(V,\ell_\infty^5).
\]
Conversely, a projection \(Q\) onto \(V\), direct-summed with the identity on coordinate six and the averaging projections \((s,t)\mapsto((s+t)/2,(s+t)/2)\) on the remaining disjoint pairs, is a projection onto \(W_n\) of norm \(\max\{\|Q\|,1\}\). Every projection onto nonzero \(V\) has norm at least one. Thus
\[
\lambda(W_n,\ell_\infty^{2n})=\lambda(V,\ell_\infty^5).
\]

**Step 2: exact parameterization of all projections needed for the lower bound.** Consider the signed coordinate permutation
\[
R(x_1,x_2,x_3,x_4,x_5)=(-x_1,x_5,x_4,x_3,x_2).
\]
It is an isometric involution with \(Ru=-u\) and \(Rv=v\). Any projection \(Q\) onto \(V\) can be replaced by \((Q+RQR)/2\), a projection onto \(V\) of no larger norm that commutes with \(R\). Such a projection can be written uniquely as \(Qx=f(x)u+g(x)v\) with coordinate functionals
\[
f=(a,b,c,-c,-b),\qquad g=(0,d,e,e,d),
\]
where \(a,b,c,d,e\in\mathbb R\). The requirements \(f(u)=1\) and \(g(v)=1\), with the cross terms vanishing by symmetry, are exactly
\[
 a+\frac85b+\frac12c=1,\qquad \frac65d+2e=1.\tag{1}
\]
The five absolute row sums are \(A,B,C,C,B\), where
\[
\begin{aligned}
 A&=|a|+2|b|+2|c|,\\
 B&=\frac{4|a|+2\max\{4|b|,3|d|\}+2\max\{4|c|,3|e|\}}5,\\
 C&=\frac{|a|}4+2\max\{|b|/4,|d|\}+2\max\{|c|/4,|e|\}.
\end{aligned}
\]
The formulas use the identity \(|r+s|+|r-s|=2\max\{|r|,|s|\}\) for real numbers. Consequently \(\|Q\|=\max\{A,B,C\}\).

**Step 3: a global dual lower certificate.** Put \(\theta=286/315\). For all real \(a,b,c,d,e\), the following lower estimates are valid, without sign assumptions:
\[
\begin{aligned}
 A&\ge a+2b+2c,\\
 B&\ge\frac{4a+8\theta b+6(1-\theta)d+6e}{5},\\
 C&\ge a/4+2d+2e.
\end{aligned}
\]
For the middle inequality use \(\max\{4|b|,3|d|\}\ge4\theta b+3(1-\theta)d\) and \(\max\{4|c|,3|e|\}\ge3e\). Every coefficient is nonnegative and \(0<\theta<1\). The other inequalities follow from \(|s|\ge s\) and \(\max(|s|,|t|)\ge t\). Now \(104+315+240=659\), so their convex combination yields
\[
\begin{aligned}
\max\{A,B,C\}
&\ge\frac{104A+315B+240C}{659}\\
&\ge\frac{416}{659}\left(a+\frac85b+\frac12c\right)
+\frac{429}{659}\left(\frac65d+2e\right)\\
&=\boxed{\frac{845}{659}},
\end{aligned}
\]
where the last equality uses the two reproduction constraints (1). Averaging does not increase the norm, so the same lower bound holds for **every**, not merely symmetric, projection onto \(V\).

**Step 4: matching projection.** Take
\[
\begin{aligned}
f_*&=(520/659,\ 105/1318,\ 110/659,\ -110/659,\ -105/1318),\\
g_*&=(0,\ 70/659,\ 575/1318,\ 575/1318,\ 70/659).
\end{aligned}
\]
Direct rational arithmetic gives \(f_*(u)=g_*(v)=1\) and \(f_*(v)=g_*(u)=0\), so
\[
Q_*x=f_*(x)u+g_*(x)v
\]
is a projection onto \(V\). Each of its five absolute row sums equals precisely \(845/659\). Therefore \(\|Q_*\|=845/659\), matching the universal lower certificate. The block extension described in Step 1 attains the same norm on every \(W_n\). Finally, the equality between relative and absolute projection constants in finite \(\ell_\infty\) embeddings [1, equation (1)] gives the claimed absolute constant. This completes the proof.

## Verification

The standalone \`CHECK.py\` uses exact rational arithmetic from the standard-library \`fractions.Fraction\` class. Run \`python3 CHECK.py\` from this directory. It checks the biorthogonality identities, all five exact row sums, idempotence, the reflection symmetry, every coefficient in the dual lower certificate, and the explicitly block-diagonal projections for the finite sample \(3\le n\le12\). It executed successfully with 2,919 exact rational assertions. These computations reproduce the finite rational certificate; the argument that no projection can do better for **all** real coefficients and **all** \(n\ge3\) is the explicit symbolic inequality in Step 3 and the dimension reduction in Step 1, not finite enumeration.

## Relationship to prior work

Deregowska and Lewandowska [1, Propositions 3.2--3.4] introduce \(W_n\) to show that a disjoint-support geometric lemma from their codimension-two argument fails in higher codimension, while a weaker projection-column condition survives. They exhibit a projection onto \(W_n\) with norm \(13/10\). The result here identifies the **optimal norm of every possible projection** for this same example. The bound \(13/10\) is not an optimality statement, and the explicit witness in [1] does not give the present dual lower certificate. Other related work on hyperplane projection gaps and projections onto structured finite metric free spaces concerns different spaces and does not imply the exact five-coordinate optimum; see the scientific comparison in the accompanying review.

## Limitations

The theorem is restricted to the indicated real five-coordinate configuration and its disjoint coordinate extensions. It neither establishes a sharp projection constant for arbitrary subspaces of \(\ell_\infty^{2n}\) nor resolves the higher-codimension Banach--Mazur conjecture in [1]. The exact certificate is self-contained, but no independent external mathematical audit or exhaustive bibliographic priority search is claimed. The source's presentation was inspected in its publicly accessible arXiv text, including the relevant Section 3 propositions; a separate PDF was not needed for the calculations.

## References

[1] B. Deregowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1 (first publicly submitted 2026-10-05), Section 3, Propositions 3.2--3.4, and equation (1). https://arxiv.org/abs/2610.06141
