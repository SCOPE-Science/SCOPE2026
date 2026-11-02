# Jordan strata and cyclic-subgroup census for the modular group algebra of \(C_3\times C_3\)

## Finding

Let \(k\) be any field of characteristic \(3\), \(G=C_3\times C_3\), and \(A=kG\). The left regular action of every nonidentity element in the normalized unit group \(U=1+J(A)\) has one of exactly five possible Jordan partitions. Equivalently, there are exactly six Jordan types for the multiplication operators \(m_f:A\longrightarrow A\) indexed by \(f\in J(A)\), including the zero operator. All six loci are smooth and geometrically irreducible. This refines the usual free-module assertion for nonzero linear shifted subgroups by classifying **all** cyclic subgroups of \(U\), including non-flat ones.

Choose generators \(h_1,h_2\) of \(G\), put \(x=h_1-1\), \(y=h_2-1\), and write each radical element uniquely as
\[
f=ux+vy+ax^2+bxy+cy^2+dx^2y+exy^2+gx^2y^2.
\]
Set \(\Delta=b^2-ac\). For a partition, \(3^j\) means \(j\) blocks of size \(3\).

| Disjoint condition | Jordan partition for \(m_f\) | Dimension | Points over \(\mathbb F_q\) |
|---|---|---:|---:|
| \((u,v)\neq(0,0)\) | \((3^3)\) | \(8\) | \((q^2-1)q^6\) |
| \(u=v=0,\ \Delta\neq0\) | \((3,2^2,1^2)\) | \(6\) | \((q^3-q^2)q^3\) |
| \(u=v=0,\ (a,b,c)\neq0,\ \Delta=0\) | \((2^3,1^3)\) | \(5\) | \((q^2-1)q^3\) |
| \(u=v=a=b=c=0,\ (d,e)\neq0\) | \((2^2,1^5)\) | \(3\) | \((q^2-1)q\) |
| \(u=v=a=b=c=d=e=0,\ g\neq0\) | \((2,1^7)\) | \(1\) | \(q-1\) |
| \(f=0\) | \((1^9)\) | \(0\) | \(1\) |

Here \(q=3^r\) for any integer \(r\geq1\), and the formulas sum to \(q^8\). The same rows, with \(q\) replaced by the Lefschetz class \(\mathbb L=[\mathbb A^1]\), give the corresponding classes in the Grothendieck ring of varieties. Every nonzero \(f\) gives a unit \(1+f\) of order three. Dividing each of the first five point counts by \(2\) gives the exact numbers of cyclic order-three subgroups of \(1+J\) of the respective Jordan types. In particular the total number is \((q^8-1)/2\).

## Assumptions and scope

The algebra is the **regular module** of the elementary abelian group of order \(9\), over an arbitrary field \(k\) of characteristic \(3\). Its augmentation radical \(J\) is \(8\)-dimensional. No algebraic-closure assumption is made. Finite-field counts concern actual \(\mathbb F_q\)-rational radical elements and subgroups, not conjugacy classes. The module being restricted is \(A\) itself. The assertions about strata are for their natural reduced locally closed algebraic varieties.

The characteristic assumption is essential: it gives the identification \(A\cong k[x,y]/(x^3,y^3)\) and the identity \(f^3=0\) for every \(f\in J\). There are no blocks longer than \(3\).

## Proof

**Step 1: reducing to ranks.** The monomials \(x^iy^j\) with \(0\leq i,j\leq2\) give a basis of dimension \(9\), and \(J^5=0\). For \(f\in J\), the Frobenius identity gives \(f^3=0\). Write \(r_1=\operatorname{rank}m_f\) and \(r_2=\operatorname{rank}m_f^2\). If the Jordan partition has \(n_j\) blocks of length \(j\), then
\[
n_3=r_2,\qquad n_2=r_1-2r_2,\qquad n_1=9-2n_2-3n_3.
\]
It therefore suffices to prove the ranks in each row of the table.

**Step 2: the nonzero linear locus.** If \((u,v)\neq0\), choose \(z\in J\) whose linear part is independent of that of \(f\). Both \(f\) and \(z\) have cube zero, so the assignments \(x\mapsto f\), \(y\mapsto z\) define an endomorphism of \(A\). Its action on \(J/J^2\) is invertible. Its graded action on the finite filtration by powers of \(J\) is consequently surjective, and hence the endomorphism is an automorphism. Conjugating multiplication by \(f\) to multiplication by \(x\) exhibits three length-three strings, one for each basis element \(1,y,y^2\) over \(k[x]/(x^3)\). Thus \((r_1,r_2)=(6,3)\), giving \((3^3)\).

**Step 3: quadratic-leading elements.** Suppose \(u=v=0\) and \(Q=ax^2+bxy+cy^2\neq0\). The image of \(m_f\) is filtered by degree. Its degree-two part is the nonzero vector \(Q\); its degree-three part is the span of \(Qx\) and \(Qy\). Relative to basis \((x^2y,xy^2)\), their coefficient matrix is
\[
T_Q=\begin{pmatrix}b&a\\c&b\end{pmatrix},\qquad \det T_Q=b^2-ac=\Delta.
\]
The degree-four part \(fJ^2\) is the entire socle \(k x^2y^2\), since the functional \((A,B,C)\mapsto cA+bB+aC\) on the degree-two monomials is nonzero. Any cancellation among leading degree-three images changes only their degree-four terms and therefore does not add further rank. Consequently
\[
\operatorname{rank}m_f=2+\operatorname{rank}T_Q
=\begin{cases}4,&\Delta\neq0,\\3,&\Delta=0.\end{cases}
\]
Moreover, the cubic and quartic terms of \(f\) do not contribute to \(f^2\), and direct multiplication gives
\[
f^2=Q^2=(b^2+2ac)x^2y^2=(b^2-ac)x^2y^2=\Delta x^2y^2.
\]
Hence \(r_2=1\) exactly when \(\Delta\neq0\), and \(r_2=0\) otherwise. The two partitions follow from Step 1.

**Step 4: higher-order elements.** If \(Q=0\) as well, let \(f=dx^2y+exy^2+gx^2y^2\). If \((d,e)\neq0\), then the image is spanned by \(f\) and the socle: multiplication of \(f\) by \(x\) and \(y\) gives \(e x^2y^2\) and \(d x^2y^2\). Thus \((r_1,r_2)=(2,0)\). If \(d=e=0,g\neq0\), then \((r_1,r_2)=(1,0)\). The zero element has \((0,0)\). Step 1 gives the final three partitions.

**Step 5: geometric and arithmetic strata.** In the quadratic coefficient space \(\mathbb A^3_k\), the equation \(b^2-ac=0\) cuts out the rank-one quadratic cone, with the vertex as its only singular point. It is absolutely irreducible: its projectivization is a smooth conic, and over any extension field a point with \(a\neq0\) is described by \(c=b^2/a\). The cone is a two-dimensional geometrically irreducible affine variety; its only point omitted by the \(Q\neq0\) stratum is the vertex, so that punctured stratum is smooth. Its rational point count is \((q-1)q+q=q^2\). The \(\Delta\neq0\) locus is its smooth geometrically irreducible complement in \(\mathbb A^3\), of size \(q^3-q^2\). The other strata are punctured affine spaces or a point, times free affine factors. This proves smoothness, irreducibility, dimensions and all six displayed cardinalities.

**Step 6: normalized units.** In characteristic three, \((1+f)^3=1+f^3=1\) for all \(f\in J\). A nonzero \(f\) therefore generates a subgroup \(\langle1+f\rangle\) of order \(3\); the other nonidentity element equals \((1+f)^2=1+(2f+f^2)\). The regular operator \(m_{2f+f^2}=m_f(2I+m_f)\) is a unit factor times \(m_f\); more strongly, \((m_{2f+f^2})^j=m_f^j(2I+m_f)^j\) has the same rank for all \(j\). Both generators therefore have identical Jordan forms. Every subgroup has exactly two nonidentity elements, giving the division-by-two formulas. In particular these include the four types with \(f\in J^2\), whose maps are not flat \(k[C_3]\)-embeddings into \(kG\).

## Verification

A standalone checker (`checks/jordan_census.py`) independently forms the original nine-dimensional multiplication table, calculates \(\operatorname{rank}m_f\) and \(\operatorname{rank}m_{f^2}\) by Gaussian elimination, and verifies the table without assuming the rank formulas. It exhausts all \(3^8=6561\) radical elements over \(\mathbb F_3\), including the five nonzero Jordan types and the zero case. Its complete multiplicities, in the order above, are \(5832,486,216,24,2,1\). It also enumerates every order-three subgroup and confirms the predicted \(3280\) subgroups and generator agreement.

The extension-field implementation uses \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). It tests \(1800\) pseudorandom radical elements and an additional \(2916\) targeted cases spanning all quadratic and cubic leading parameters. In both fields it independently enumerates the discriminant-zero quadratic forms, obtaining \(q^2\) as predicted. All tests passed; the marker is `MODULAR_C3xC3_MULTIPLICATION_JORDAN_OK`. Only the \(\mathbb F_3\) full-element count is exhaustive; all general-field and all-\(q\) claims rely on the displayed proof, not on finite computation.

To replay, execute `python3 checks/jordan_census.py` using Python's standard library. The expected output is embedded as `checks/output.txt`.

## Relationship to prior work

The use of Jordan types for modules over elementary abelian \(p\)-group algebras is established. The 2011 article by Öztürk Kaptanoğlu proves p-point invariance results for \(k[C_p\times C_p]\)-modules and explicitly distinguishes p-points, which have nonzero first-order radical part, from arbitrary radical points. It implies the familiar free restriction for the regular module on the first row, but does not state the four non-flat strata or their arithmetic multiplicities. Carlson–Friedlander–Suslin's 2011 work develops constant Jordan type and related invariants of such modules, again in the p-point setting. Baland–Chan's 2015 treatment emphasizes shifted subgroup embeddings with linearly independent images in \(J/J^2\), so those statements cannot apply to subgroups generated by elements of \(J^2\). These existing results are not claimed as new.

Anthony Iarrobino’s January 2020 lecture slides use precisely \(k[x,y]/(x^3,y^3)\) to demonstrate characteristic-dependent Jordan types and explicitly show \((3^3)\) for multiplication by \(x\). This is a direct prior instance of the first row, not a classification of elements in \(J^2\) or a census of normalized-unit subgroups. The new assessed claim is the **joint** complete classification of the nonlinear radical locus, its discriminant-controlled Jordan transition, its smooth geometric strata and precise cyclic-subgroup census over every characteristic-three finite field. Searches of closely related published statements did not find an implication establishing this complete result. This is a best-knowledge originality assessment, not a guarantee of historical priority.

## Limitations

The classification uses the nine-dimensional regular module of exactly \(C_3\times C_3\) in characteristic \(3\); no claim is made for arbitrary modules, groups of higher order, characteristic \(2\), or higher nilpotency exponent. The theorem does not classify conjugacy orbits of subgroup embeddings under automorphisms of the algebra. The strata are viewed as reduced varieties; scheme-theoretic multiplicities of rank-determinantal loci are not evaluated. Independent mathematical verification and exhaustive historical priority review have not been performed.

## References

1. S. Baland and K. Chan, *Modules of constant Jordan type, pullbacks of bundles and generic kernel filtrations*, arXiv:1504.01994v1 (initial public submission 2015-04-08). https://arxiv.org/abs/1504.01994
2. S. Öztürk Kaptanoğlu, *Jordan type of a k[Cp×Cp]-module*, New York Journal of Mathematics 17a (2011), 307–313. https://nyjm.albany.edu/j/2011/17a-18v.pdf
3. J. F. Carlson, E. M. Friedlander and A. Suslin, *Modules for Z/p × Z/p*, Commentarii Mathematici Helvetici 86 (2011), 609–657, doi:10.4171/CMH/236. https://ems.press/content/serial-article-files/43265
4. A. Iarrobino, *Jordan type and Artinian Gorenstein algebras*, Dalhousie lecture slides (2020-01-25), especially slides 5–6 on \(k[x,y]/(x^3,y^3)\). https://www.mscs.dal.ca/~faridi/research/inverse_systems/Dalhousie-2020/Tony-Iarrobino-Talk.pdf
