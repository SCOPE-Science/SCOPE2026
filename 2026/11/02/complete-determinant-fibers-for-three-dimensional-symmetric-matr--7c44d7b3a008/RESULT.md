# Complete determinant fibers for three-dimensional symmetric matrices with prescribed diagonal

## Finding

Let \(q\) be any odd prime power, \(F=\mathbb F_q\), and \(\chi:F\to\{-1,0,1\}\) its quadratic character, extended by \(\chi(0)=0\). For \(a,b,c,\delta\in F\), define

\[
N_{a,b,c}(\delta)=\#\left\{(x,y,z)\in F^3:
\det\begin{pmatrix}a&x&y\\x&b&z\\y&z&c\end{pmatrix}=\delta\right\}.
\]

Put \(k=\mathbf1_{a\ne0}+\mathbf1_{b\ne0}+\mathbf1_{c\ne0}\) and \(P=abc\). **For every nonzero \(\delta\in F\), the complete determinant-fiber law is**

\[
\boxed{N_{a,b,c}(\delta)=q^2+1+q\left[
\chi(-\delta a)+\chi(-\delta b)+\chi(-\delta c)
+\mathbf1_{k=3}\chi\bigl(\delta(\delta-P)\bigr)-\max(2-k,0)
\right].}
\]

**For \(\delta=0\), the exact singular-fiber law is**

\[
\boxed{N_{a,b,c}(0)=
\begin{cases}
3q^2-3q+1,&k=0,\\
2q^2-2q+1,&k=1,\\
q^2-q+1,&k=2,\\
q^2+1,&k=3.
\end{cases}}
\]

Thus the number of singular matrices with a prescribed diagonal depends only on the *number* of nonzero prescribed entries, although the nonzero determinant fibers can depend sharply on their values and square classes. For example, over \(\mathbb F_5\) with all three diagonal entries equal to \(1\), the fiber sizes at determinants \(0,1,2,3,4\) respectively are \(26,41,6,16,36\).

## Assumptions and scope

All field operations are in \(\mathbb F_q\). The result holds for every odd prime power, including nonprime fields, without assumptions on the three prescribed diagonal entries. The matrix is symmetric, and exactly its three *off-diagonal* entries vary freely. There are precisely \(q^3\) such matrices for a fixed diagonal. Characteristic two is excluded: in that characteristic the determinant expansion loses its \(2xyz\) term and the quadratic-character classification does not apply.

## Proof

**A binary quadratic-form count.** For nonzero \(d\in F\), let \(Q(Y,W)=-(d/a)Y^2-aW^2\), where \(a\ne0\). Its determinant as a quadratic form is \(d\). The number of solutions of \(Q(Y,W)=t\) is

\[
q-\chi(-d)+q\chi(-d)\mathbf1_{t=0}.
\]

Indeed, for a nondegenerate binary diagonal form \(uY^2+vW^2\) with \(uv\ne0\), a one-variable quadratic-character sum gives \(q-\chi(-uv)\) solutions for \(t\ne0\) and \(q+(q-1)\chi(-uv)\) for \(t=0\). The character identity needed here is \(\sum_{s\in F}\chi(s^2-D)=-1\) whenever \(D\ne0\): the number of ordered pairs \((s,t)\) with \(t^2=s^2-D\) equals the number \(q-1\) of pairs of nonzero factors \((s-t)(s+t)=D\), since \(2\) is invertible.

**At least two nonzero diagonal entries.** By simultaneously permuting rows and columns, take \(a,b\ne0\). Set \(d=ab-x^2\) and \(w=z-xy/a\). Direct expansion and completion of the square yield

\[
\det\begin{pmatrix}a&x&y\\x&b&z\\y&z&c\end{pmatrix}
=dc-(d/a)y^2-aw^2.
\]

For \(d\ne0\), the binary quadratic-form count gives \(q-\chi(-d)+q\chi(-d)\mathbf1_{\delta=dc}\) choices of \((y,z)\). For \(d=0\), the determinant equals \(-aw^2\), and for any \(\delta\) the number of \((y,z)\) is \(q(1+\chi(-\delta/a))\). There are \(R=1+\chi(ab)\) values of \(x\) with \(d=0\), and the identity \(\sum_{x\in F}\chi(x^2-ab)=-1\) gives

\[
\sum_{x:d\ne0}(q-\chi(-d))=q(q-R)+1.
\]

Fix \(\delta\ne0\). If \(c=0\), there is no \(d\) with \(dc=\delta\). Hence the above contributions sum to

\[
q^2+1+q(\chi(-\delta a)+\chi(-\delta b)).
\]

Here we used \(R\chi(-\delta/a)=\chi(-\delta a)+\chi(-\delta b)\), valid because \(a,b\ne0\) and \(\chi\) is multiplicative. If \(c\ne0\), the additional \(d=\delta/c\) term contributes

\[
q\chi(-\delta/c)\bigl(1+\chi(ab-\delta/c)\bigr)
=q\left[\chi(-\delta c)+\chi\bigl(\delta(\delta-abc)\bigr)\right].
\]

This proves the asserted nonzero-fiber formulas when \(k=2\) or \(k=3\).

**At most one nonzero diagonal entry.** If \(k=1\), assume \(a=b=0\), \(c\ne0\). The determinant becomes \(x(2yz-cx)\). For \(\delta\ne0\), necessarily \(x\ne0\). Given \(x\), the equation \(yz=(\delta/x+cx)/2\) has \(q-1\) solutions unless its right-hand side is zero, when it has \(2q-1\). Therefore

\[
N_{0,0,c}(\delta)=(q-1)^2+q(1+\chi(-\delta/c))
=q^2-q+1+q\chi(-\delta c).
\]

If \(k=0\), the determinant is \(2xyz\). For each \(\delta\ne0\), exactly \((q-1)^2\) triples give that determinant. Both cases coincide with the boxed formula.

**The zero fibers.** For each fixed diagonal, sum the nonzero-fiber formula over \(\delta\in F^\times\) and subtract from \(q^3\). The linear-character terms have zero sum. When \(k=3\), the remaining extra sum equals

\[
\sum_{\delta\in F^\times}\chi\bigl(\delta(\delta-P)\bigr)=-1,
\qquad P\ne0,
\]

by the quadratic-character identity above. Thus, for \(k=3\), the nonzero fibers sum to \((q-1)(q^2+1)-q\), giving \(N(0)=q^2+1\). For \(k=2,1,0\) the sums are respectively \((q-1)(q^2+1)\), \((q-1)(q^2-q+1)\), and \((q-1)^3\), producing the remaining three displayed zero-fiber values. This finishes the proof.

## Verification

The standalone file `verify.py` evaluates the determinant from its six Leibniz terms, independently of the proof's quadratic-form reduction. It exhaustively enumerates all prescribed diagonals and all off-diagonal triples over the prime fields of sizes \(3,5,7,11\), and tests eight diagonals over \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). It checks every nonzero fiber and every singular fiber against the displayed formulas using exact integer and finite-field arithmetic. The executed run reported `VERIFY_OK prime_fields=3,5,7,11 extension_field=9 determinant_fibers=17820 independent_matrices=1911396 singular_and_nonzero_cases=yes`. These computations corroborate, but do not replace, the general proof.

## Relationship to prior work

Gorodetsky's 2026 Theorem 1.4 counts *unrestricted invertible matrices* with prescribed diagonal, without conditioning on determinant and without requiring symmetry. The present law counts the different family of symmetric \(3\)-by-\(3\) matrices, resolves each determinant fiber rather than just their union, and explicitly exhibits quadratic-character variation. Li and Hu (2011) evaluate determinant-twisted additive sums on the full general linear group; their formulas do not impose the symmetric-matrix constraint. Brent and McKay (1988/2010) count symmetric matrices by determinant divisibility without conditioning on the diagonal, a coarser statistic which does not determine the conditional fibers here. The older matrix-exponential-sum literature, notably Hodges (1955), may contain implicit related evaluations; priority relative to that inaccessible source has not been independently resolved.

## Limitations

The formula is confined to dimension three and odd characteristic, and does not classify prescribed *off-diagonal* patterns or higher-rank symmetric matrices. The elementary proof establishes the count in full generality within this scope. The literature comparison is a best-knowledge originality assessment, not an independent priority certification; the full text of Hodges (1955) was not obtainable in the available research access.

## References

1. O. Gorodetsky, *Statistics of entries of matrices from the general linear group over a finite field*, arXiv:2610.29305v1 (public 2026-10-21), especially Theorem 1.4. https://arxiv.org/html/2610.29305v1
2. Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1 (2011), especially Theorem 2.1 and the determinant-twisted sum in equation (2.12). https://arxiv.org/pdf/1105.4513
3. R. P. Brent and B. D. McKay, *On determinants of random symmetric matrices over Z_m*, 1988 technical report, arXiv:1004.5440v1 (2010), Introduction and Section 2. https://arxiv.org/pdf/1004.5440
4. J. H. Hodges, *Exponential sums for symmetric matrices in a finite field*, *Mathematische Nachrichten* 14 (1955), 331–339, DOI:10.1002/mana.19550140411. Publisher metadata consulted; full text unavailable.
5. D. S. Kim, *Gauss sums for O-minus(2n,q)*, *Acta Arithmetica* 80 (1997), 343–365, Introduction (discussion of Hodges's generalized matrix sums). https://matwbn.icm.edu.pl/ksiazki/aa/aa80/aa8044.pdf
