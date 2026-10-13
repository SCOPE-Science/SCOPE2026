# Exact square-word membership and image size in \(UT_5\) over characteristic-two fields

## Finding

Let \(k=\mathbb F_q\) with \(q=2^e\), where \(e\ge1\), and let \(U=UT_5(k)\) be the group of unitriangular \(5\times5\) matrices. Define \(S=\{g^2:g\in U\}\) and \(D=[U,U]\). The following gives the **complete target-by-target square-root criterion in the distinguished upper-triangular flag**, together with the size of the word-map image, for every characteristic-two finite field.

Identify the derived group with the six-coordinate set
\[
Y(u,v,w,r,s,t)=I+uE_{13}+vE_{24}+wE_{35}+rE_{14}+sE_{25}+tE_{15}.
\]
The **complete square criterion** is
\[
Y(u,v,w,r,s,t)\in S\iff
\big(v=0\text{ and }uw=0\big)
\ \text{or}\ 
\big(v\ne0\text{ and }((u,w)\ne(0,0)\text{ or }vt=rs)\big).
\]
Consequently,
\[
|S|=q^6-q^5+q^4+q^3-q^2,
\qquad |D\setminus S|=q^2(q-1)(q^2-1).
\]
The square-word image distinguishes unipotent matrices whose nilpotent parts have identical Jordan type: \(I+E_{13}+E_{25}\) is a square in \(U\) but \(I+E_{24}+E_{15}\) is not, although both nilpotent parts are square-zero, rank two, and have Jordan type \((2,2,1)\).

## Assumptions and scope

All groups are over an arbitrary finite field of characteristic two. Here \(E_{ij}\) denotes the matrix unit in row \(i\), column \(j\); multiplication is ordinary matrix multiplication. A group square means \(g^2\) for one group element \(g\), rather than an additive square. All counts concern **distinct image elements**, not numbers of square roots.

## Proof

**First-superdiagonal reduction.** Write \(g=I+N\) with \(N\) strictly upper triangular. Characteristic two gives \((I+N)^2=I+N^2\), whose first superdiagonal vanishes. Thus \(S\subseteq D\). Conversely, elementary commutators of transvections generate every matrix unit on superdiagonals of distance at least two, so \(D\) consists exactly of the matrices with zero first superdiagonal. This description is valid in every characteristic.

**The six-coordinate square equations.** Write
\[
\begin{aligned}
&a=N_{12},\ b=N_{23},\ c=N_{34},\ d=N_{45},\\
&e=N_{13},\ f=N_{24},\ g=N_{35},\\
&h=N_{14},\ i=N_{25},\ j=N_{15}.
\end{aligned}
\]
Direct multiplication, including all paths of length two, gives exactly
\[
\boxed{u=ab,\quad v=bc,\quad w=cd,\quad r=af+ec,\quad s=bg+fd,\quad t=ai+eg+hd.}
\]
The entries \(j\) and every expression involving paths longer than two are irrelevant to \(N^2\).

**Necessity of the criterion.** If \(v=bc=0\), then \(u=ab\) and \(w=cd\) cannot both be nonzero, since that would force \(b,c\ne0\). If \(v\ne0\) and \(u=w=0\), then \(b,c\ne0\) and \(a=d=0\). Thus \(r=ec\), \(s=bg\), and \(t=eg\), yielding \(vt=(bc)(eg)=(ec)(bg)=rs\). No other restrictions have been used.

**Sufficiency, by explicit roots.** If \(v\ne0\), set \(b=1\), \(c=v\), \(a=u\), \(d=w/v\), \(f=0\), \(e=r/v\), and \(g=s\). These choices give the prescribed \(u,v,w,r,s\). The last equation becomes \(t=ui+rs/v+(w/v)h\). If \((u,w)\ne(0,0)\), at least one of \(i,h\) solves it; when \((u,w)=(0,0)\), it is solvable precisely when \(vt=rs\).

If \(v=0\), the necessary relation \(uw=0\) leaves three cases. When \(u\ne0\), let \(a=1,b=u,c=d=e=0,f=r,g=s/u,i=t\) and take \(h=j=0\). When \(w\ne0\), let \(a=b=0,c=1,d=w,e=r,f=s/w,g=0,h=t/w\) and take \(i=j=0\). Finally, if \(u=w=0\) and \((r,s)\ne(0,0)\), let \(a=r,d=s,b=c=0,f=1,e=g=0\), choosing \(i,h\) to satisfy \(ri+sh=t\). If \(u=w=r=s=0\), let \(a=1,b=c=d=e=f=g=h=0,i=t\). In every case set unspecified entries to zero. These constructions give a strictly upper-triangular \(N\) with \(N^2=Y-I\). Hence the criterion is both necessary and sufficient over every field \(k\) of characteristic two.

**Counting distinct image elements.** If \(v=0\), there are \(2q-1\) possible pairs \((u,w)\), and \(q^3\) independent choices for \((r,s,t)\). If \(v\ne0\), the \(q^2-1\) nonzero pairs \((u,w)\) allow \(q^3\) triples \((r,s,t)\); at \((u,w)=(0,0)\), the relation \(vt=rs\) allows \(q^2\) triples. Therefore
\[
(2q-1)q^3+(q-1)((q^2-1)q^3+q^2)
=q^6-q^5+q^4+q^3-q^2.
\]
Since \(|D|=q^6\), subtraction gives the number of nonsquares.

**Identical Jordan type but opposite status.** The nilpotent parts \(E_{13}+E_{25}\) and \(E_{24}+E_{15}\) both have square zero and rank two and hence Jordan shape \((2,2,1)\). The first is \(N^2\) for \(N=E_{12}+E_{23}+E_{35}\). The second violates the criterion with \(v=t=1\), \(r=s=0\). It does have a square root after forgetting the distinguished flag: a \(4\times4\) nilpotent Jordan block plus a zero block has square of Jordan type \((2,2,1)\). The obstruction is therefore flag-sensitive.

## Verification

The standalone checker `verify_square_word.py` uses exact multiplication tables for \(\mathbb F_2\) and \(\mathbb F_4\). It exhaustively enumerates all \(q^{10}\) strictly upper-triangular \(5\times5\) matrices, computes every square image and fiber, compares each of the \(q^6\) possible targets with the iff criterion, and verifies the total image size and two-square coverage. It also verifies \(S_4=D_4\). The outputs are \(52\) squares of \(64\) derived elements at \(q=2\), and \(3376\) squares of \(4096\) derived elements at \(q=4\). All enumerated checks pass.

Finite enumeration does not establish the universal \(q\)- or \(n\)-quantifiers. Those follow from the reversible equations, explicit constructions, and projection argument proved above.

## Relationship to prior work

The known background must be separated sharply from the present result. Bier (2012, Theorems 2–3) proves the lower-central-subgroup identity and verbal width for power words in unitriangular groups: at characteristic two the sharp width two in size five is **already known**. Dolfi–Singh–Yadav (2019, Proposition 3.4 and Theorem A) prove the first strict-power-image threshold at size five and study its lower bound; their numerical table explicitly lists \(52\) elements for \(q=2\) and \(3376\) for \(q=4\). None of these results, nor those two tabulated numerical values, is claimed new here.

The contribution addressed here is the **complete six-coordinate necessary-and-sufficient square membership criterion** and its exact polynomial image size over **every** characteristic-two finite field, including extension degrees not in that table. A lower bound, two samples, and the verbal-width theorem cannot determine the individual image membership for all \(q^6\) targets or the general polynomial without additional work. The complete image description answers the inverse problem implicit in the existing study of power-word images. Marberg supplies normal-pattern subgroup context, while Hesselink and Öztürk address nilpotent matrices with flags and unrestricted roots, respectively; the latter two do not supply the fixed-flag square membership distinction exhibited here.

## Limitations

The complete membership criterion and exact image polynomial are proved for size five and characteristic two only. Their generalization to larger unitriangular groups and odd characteristic is not asserted. Known threshold and verbal-width results, as well as the two published small-field counts, are expressly credited; these are not asserted as original. The comparison to published material cannot exclude an equivalent result under different word-map or flag terminology; independent validation has not been performed.

## References

1. E. Marberg, *Superclasses and supercharacters of normal pattern subgroups of the unipotent upper triangular matrix group*, arXiv:1005.4151 (first public version 22 May 2010), https://arxiv.org/abs/1005.4151.
2. A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389 (first public version 19 November 2014), https://arxiv.org/abs/1411.5389.
3. W. H. Hesselink, *A classification of the nilpotent triangular matrices*, Compositio Mathematica 55 (1985), 89–133, https://www.numdam.org/item/CM_1985__55_1_89_0/.
4. S. Öztürk, *On m-th roots of nilpotent matrices*, Electronic Journal of Linear Algebra 37 (2021), 718–733, DOI:10.13001/ela.2021.6331.
5. A. Bier, *The width of verbal subgroups in the group of unitriangular matrices over a field*, International Journal of Algebra and Computation 22 (2012), article 1250019, DOI:10.1142/S0218196712500191.
6. S. Dolfi, A. Singh, M. K. Yadav, *\(p\)-Power conjugacy classes in \(U(n,q)\) and \(T(n,q)\)*, arXiv:1905.04244 (first public version 10 May 2019), https://arxiv.org/abs/1905.04244.
