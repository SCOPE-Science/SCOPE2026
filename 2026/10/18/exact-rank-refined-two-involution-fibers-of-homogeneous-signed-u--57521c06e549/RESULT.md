# Exact rank-refined two-involution fibers of homogeneous signed-unipotent matrices over odd finite fields

## Finding

Let \(q\) be an odd prime power, \(n\ge2\), and \(m\ge1\). Let \(J\) be the direct sum of \(m\) unipotent Jordan blocks of size \(n\) on \(V=\mathbb F_q^{nm}\). Put \(d=nm\) and \(g_\varepsilon=\varepsilon J\) for \(\varepsilon=\pm1\). Involutions are matrices satisfying \(s^2=I\), including the identity. For \(st=g_\varepsilon\), define \(r(s)\) to be the dimension of the positive eigenspace of \(s\) on \(V/(g_\varepsilon-\varepsilon I)V\). This quotient is \(m\)-dimensional. It carries the action of \(s\), because \(sJs=J^{-1}\) and \((J^{-1}-I)V=(J-I)V\).

For \(0\le r\le m\), set
\[
N_r=\begin{cases}
{m\brack r}_q\,q^{km^2+r(m-r)},&n=2k+1,\\
{m\brack r}_q\,q^{km^2-r(m-r)},&n=2k,
\end{cases}
\qquad
a_r=\begin{cases}km+r,&n=2k+1,\\km,&n=2k.\end{cases}
\]
Here \({m\brack r}_q\) is the Gaussian binomial coefficient. The exact prescribed-product fiber enumerator is
\[
\sum_{\substack{s^2=t^2=I\\st=g_\varepsilon}}
u^{r(s)}z^{\dim\ker(s-I)}w^{\dim\ker(t-I)}
=\sum_{r=0}^m N_r u^r z^{a_r} w^{b_{\varepsilon,r}},
\qquad b_{1,r}=a_r,\quad b_{-1,r}=d-a_r.
\]
For positive unipotent products the factors have equal positive eigenspace dimensions; for negative products their dimensions are complementary. When \(n\) is even, the two positive dimensions are both \(km\) for every factorization. The residual rank still distinguishes \(m+1\) strata; their sizes are not all equal for \(m\ge2\). For \(m=1\), the two strata both have size \(q^k\) in either parity.

For example, at \(q=3,n=2,m=2\) the residual-rank polynomial is \(81+108u+81u^2\), with 270 ordered factorizations, all with two-dimensional positive eigenspaces. At \(q=3,n=3,m=2\), the sizes are \(81,972,81\), with positive eigenspace dimensions of \(s\) equal to \(2,3,4\), respectively.

## Assumptions and scope

The characteristic is odd and all Jordan blocks in the target have the same size. The target is a fixed matrix, not a similarity class. The coefficients count ordered pairs of matrices in its fiber, not orbits of pairs up to simultaneous similarity. The rank parameters are eigenspace dimensions over \(\mathbb F_q\), evaluated as integers. MSC2020: 15A23.

## Proof

**1. Reversing involutions.** If \(s^2=t^2=I\) and \(st=g_\varepsilon\), then \(sg_\varepsilon s=g_\varepsilon^{-1}\). Conversely an involution satisfying that relation determines the unique second factor \(t=sg_\varepsilon\), which satisfies \(t^2=I\). The sign of the product cancels out of the reversing relation, so it suffices to count the involutions reversing \(J\).

**2. Truncated-ring model.** Write \(R=\mathbb F_q[x]/(x^n)\), identify \(V=R^m\), and let \(J\) act as multiplication by \(1+x\). The ring automorphism
\[
\sigma(x)=(1+x)^{-1}-1=-x+x^2-\cdots+(-1)^{n-1}x^{n-1}
\]
satisfies \(\sigma^2=1\) and acts on \(R^m\) entrywise. The reversing relation says that \(s\) is \(\sigma\)-semilinear on \(R^m\). Thus \(s=A\sigma\) for a unique \(A\in\mathrm{GL}_m(R)\), and its involution equation is \(A\sigma(A)=I\). Its residual action on \(R^m/xR^m\) is \(A_0=A\bmod x\), an involution over \(\mathbb F_q\). If the positive dimension there is \(r\), then \(A_0\) is conjugate to \(S=\operatorname{diag}(I_r,-I_{m-r})\).

**3. One orbit per residual rank.** Conjugate by a constant matrix so \(A\equiv S\pmod{x}\). Suppose \(A\equiv S\pmod{x^j}\), where \(1\le j<n\). Write \(A\equiv S+x^jD\pmod{x^{j+1}}\). Since \(\sigma(x)^j\equiv(-1)^j x^j\pmod{x^{j+1}}\), the equation \(A\sigma(A)=I\) gives \(DS+(-1)^j SD=0\). Conjugation of \(A\sigma\) by \(U=I+x^jY\) replaces \(A\) by \(UA\sigma(U)^{-1}\) and changes the order-\(j\) coefficient to \(D+YS-(-1)^j SY\). Taking \(Y=-DS/2\) makes this zero. Iteration gives the representative \(S\sigma\). Distinct residual ranks cannot be conjugate by \(\mathrm{GL}_m(R)\), the centralizer of \(J\). Each rank occurs since \(S\sigma\) is an involution for every \(r\).

**4. Sizes of the fixed-product strata.** For \(h=m-r\), the stabilizer in \(\mathrm{GL}_m(R)\) is the fixed group of \(U\mapsto S\sigma(U)S\). Modulo \(x\) the fixed invertible matrices are \(\mathrm{GL}_r(q)\times\mathrm{GL}_h(q)\), using the trivial group in size zero. Every invariant matrix modulo \(x^j\) with invertible reduction modulo \(x\) lifts invariantly modulo \(x^{j+1}\): take any lift and average it with its image under this linear involution. The average still has the given invertible reduction. For each such lift the differences between invariant lifts are parametrized by the fixed space of \(Y\mapsto(-1)^j SYS\) on the coefficient of \(x^j\). This space consists of the diagonal blocks for even \(j\), with dimension \(r^2+h^2\), and the off-diagonal blocks for odd \(j\), with dimension \(2rh\). If \(E,O\) count even and odd integers among \(1,\ldots,n-1\), the stabilizer therefore has order
\[
|\mathrm{GL}_r(q)|\,|\mathrm{GL}_h(q)|\,q^{E(r^2+h^2)+O(2rh)}.
\]
All matrices over \(R\) with invertible reduction are invertible, so \(|\mathrm{GL}_m(R)|=q^{(n-1)m^2}|\mathrm{GL}_m(q)|\). The ratio \(|\mathrm{GL}_m(q)|/(|\mathrm{GL}_r(q)||\mathrm{GL}_h(q)|)\) counts ordered complementary subspaces of dimensions \(r,h\): choose the \(r\)-space in \({m\brack r}_q\) ways, then choose a complement in \(q^{rh}\) ways, as a graph of a map from one chosen complement to the \(r\)-space. Orbit–stabilizer now gives \(N_r\): use \(E=O=k\) for \(n=2k+1\), and \(E=k-1, O=k\) for \(n=2k\). For even \(n\) and \(m\ge2\), \(N_1/N_0=(1+q+\cdots+q^{m-1})/q^{m-1}>1\). The two \(m=1\) values follow by substitution.

**5. Integer eigenspace dimensions.** If a linear involution preserves a filtration, the dimension of its positive eigenspace is the sum of the positive dimensions on the successive layers. In fact, each short exact sequence of invariant subspaces and quotients remains exact on positive eigenspaces: a lift of a positive vector in the quotient projects to a positive lift under \((I+s)/2\) (or the corresponding projector for the involution in question). For \(s=S\sigma\), the action on \(x^jR^m/x^{j+1}R^m\) is \((-1)^j S\). Therefore that layer contributes \(r\) in even degree and \(h\) in odd degree. For even \(n=2k\) their integer sum is \(kr+kh=km\); for odd \(n=2k+1\) it is \((k+1)r+kh=km+r\). Because \(J=1+x\) acts as identity on every layer, the involution \(sJ\) has the same positive dimension. The involution \(-sJ\) exchanges the positive and negative eigenspaces of \(sJ\), giving dimension \(d-a_r\). Conjugating a general reverser into the representative uses a matrix commuting with \(J\), so both factor dimensions transfer to the original pair. The formula follows by summing over the strata, without taking a finite-field trace as an integer.

## Verification

The accompanying \(\texttt{checker.py}\) enumerates coefficient matrices in the truncated-ring model over the prime fields of orders 3 and 5, tests \(A\sigma(A)=I\), and computes the residual and positive eigenspace dimensions by exact finite-field rank. Its reported final line is `ALL_EXACT_CHECKS_PASSED 13` for thirteen cases. The checker does not test arbitrary extension fields or unbounded dimensions; the general statement follows from the algebraic argument above.

## Relationship to prior work and limitations

The qualitative criterion for products of two involutions, namely similarity to the inverse, is classical, and de Seguins Pazzis gives an elementary treatment of bireflectionality. Gill and Singh count real and strongly real conjugacy classes in finite linear groups (e.g. Theorem 3.8), not the ordered pairs for a specified target. Marques de Sá's §§5–6 give canonical forms and orbit and factor-similarity information, including for signed-unipotent products. In particular the residual-orbit and ordinary-rank support conclusions are not claimed as new. The finite-field contribution here is to compute the number of pairs in each of those strata, via the stabilizer orders, including when distinct residual ranks have the same ordinary ranks. Work on regular semisimple targets concerns different centralizers. No absolute priority claim is made.

The result does not address mixed Jordan-block sizes, characteristic two, or targets with further eigenvalues.

## References

1. Clément de Seguins Pazzis, *A note on bireflectional elements of an algebra*, arXiv:2303.00820, 2023.
2. Eduardo Marques de Sá, *Canonical Forms for Simultaneous Similarity of Pairs of Involutions*, University of Coimbra preprint 16-04, 2016, §§5–6, https://www.mat.uc.pt/preprints/ps/p1604.pdf.
3. Nick Gill and Anupam Singh, *Real and strongly real classes in finite linear groups*, arXiv:0809.4412v2, 2009.
4. Cheryl E. Praeger and Ákos Seress, *Regular semisimple elements and involutions in finite general linear groups of odd characteristic*.
