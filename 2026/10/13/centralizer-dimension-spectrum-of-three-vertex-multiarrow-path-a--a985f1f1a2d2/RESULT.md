# Centralizer-dimension spectrum of three-vertex multiarrow path algebras

## Finding

Let \(q\) be any prime power and let \(r,s\ge 2\). Let \(Q_{r,s}\) have vertices \(1,2,3\), with \(r\) parallel arrows \(1\to2\), \(s\) parallel arrows \(2\to3\), and no other arrows. Its ordinary (not radical-square-zero) path algebra is \(A=\mathbb F_q Q_{r,s}\). Put \(h=rs\) and \(D=3+r+s+h\). Define the **centralizer-dimension enumerator**
\[
H_{r,s,q}(T)=\sum_{u\in A}T^{\dim_{\mathbb F_q}C_A(u)},\qquad C_A(u)=\{v\in A:uv=vu\}.
\]
The following table determines this entire polynomial for every \(q,r,s\) in the stated range. Every row contributes \(mT^c\), where \(m\) and \(c\) are its final two entries; rows with the same \(c\) are added.

Identify the coefficient spaces of the two arrow families with \(V=\mathbb F_q^r\) and \(W=\mathbb F_q^s\), and the length-two path space with \(Z=V\otimes W\). Represent an element as \((a,b,c;x,y,z)\), with diagonal scalars \(a,b,c\) and \((x,y,z)\in V\times W\times Z\). In the row \(a=c\ne b\), set \(\alpha=a-b\ne0\) and \(z_*=z+\alpha^{-1}x\otimes y\).

| Diagonal condition | Additional condition | Multiplicity \(m\) | Centralizer dimension \(c\) |
|---|---|---:|---:|
| Pairwise distinct | Any radical | \(q(q-1)(q-2)q^{r+s+h}\) | \(3\) |
| \(a=b\ne c\) | \(x=0\) | \(q(q-1)q^{s+h}\) | \(r+3\) |
| \(a=b\ne c\) | \(x\ne0\) | \(q(q-1)(q^r-1)q^{s+h}\) | \(r+2\) |
| \(b=c\ne a\) | \(y=0\) | \(q(q-1)q^{r+h}\) | \(s+3\) |
| \(b=c\ne a\) | \(y\ne0\) | \(q(q-1)(q^s-1)q^{r+h}\) | \(s+2\) |
| \(a=c\ne b\) | \(z_*=0\) | \(q(q-1)q^{r+s}\) | \(h+3\) |
| \(a=c\ne b\) | \(z_*\ne0\) | \(q(q-1)(q^h-1)q^{r+s}\) | \(h+2\) |
| \(a=b=c\) | \(x=y=z=0\) | \(q\) | \(D\) |
| \(a=b=c\) | \(x=y=0,\ z\ne0\) | \(q(q^h-1)\) | \(D-1\) |
| \(a=b=c\) | \(x\ne0,y=0,z\in x\otimes W\) | \(q(q^r-1)q^s\) | \(h+r+2\) |
| \(a=b=c\) | \(x\ne0,y=0,z\notin x\otimes W\) | \(q(q^r-1)(q^h-q^s)\) | \(h+r+1\) |
| \(a=b=c\) | \(x=0,y\ne0,z\in V\otimes y\) | \(q(q^s-1)q^r\) | \(h+s+2\) |
| \(a=b=c\) | \(x=0,y\ne0,z\notin V\otimes y\) | \(q(q^s-1)(q^h-q^r)\) | \(h+s+1\) |
| \(a=b=c\) | \(x\ne0,y\ne0\) | \(q(q^r-1)(q^s-1)q^h\) | \(h+2\) |

In particular, the exact commuting-pair number and probability are
\[
\#\{(u,v)\in A^2:uv=vu\}=H_{r,s,q}(q),\qquad
\operatorname{Pr}(A)=\frac{H_{r,s,q}(q)}{q^{2D}}.
\]
For \((q,r,s)=(2,2,2)\), the centralizer-dimension distribution is
\[
H_{2,2,2}(T)=768T^4+256T^5+768T^6+176T^7+48T^8+30T^{10}+2T^{11},
\]
and the commuting probability is \(17/512\). The spectrum depends on the two arrow multiplicities, not just the vector-space dimension of the algebra. For example, at \(q=2\), both \(A_{2,7}\) and \(A_{3,5}\) have dimension \(26\), but their commuting probabilities are respectively
\[
\frac{305449}{67108864}\qquad\text{and}\qquad\frac{160447}{67108864}.
\]

## Assumptions and scope

All statements concern finite-dimensional associative unital path algebras over \(\mathbb F_q\). Every distinct pair of consecutive arrows represents its own path of length two; there are no relations killing these products. The theorem requires \(r,s\ge2\), and includes all finite-field characteristics. The variables \(a,b,c\) denote scalar vertex coefficients, not matrices. The enumeration counts elements by the dimension of their full *algebra* centralizer, not by the number of distinct centralizer subalgebras or by unit-group conjugacy classes.

## Proof

The basis comprises the three trivial paths, the \(r+s\) arrows, and the \(h=rs\) distinct paths of length two. If \(u=(a,b,c;x,y,z)\) and \(v=(a',b',c';x',y',z')\), multiplication is
\[
uv=(aa',bb',cc';\ ax'+xb',\ by'+yc',\ az'+zc'+x\otimes y').
\]
Set \(\delta_1=a'-b'\), \(\delta_2=b'-c'\). The commutator vanishes exactly when
\[
(a-b)x'-\delta_1x=0,\quad
(b-c)y'-\delta_2y=0,\quad
(a-c)z'-(\delta_1+\delta_2)z+x\otimes y'-x'\otimes y=0.
\tag{1}
\]
The common scalar part of \((a',b',c')\) supplies one free dimension beyond \((\delta_1,\delta_2)\).

**Pairwise distinct diagonals.** The first two equations determine \(x'\) and \(y'\) from \(\delta_1,\delta_2\). Since \(a-c\ne0\), the last determines \(z'\). Thus \(\dim C_A(u)=3\), with \(q^{r+s+h}\) radical choices for each of \(q(q-1)(q-2)\) diagonal triples.

**Exactly two equal diagonals.** If \(a=b\ne c\), then the second equation determines \(y'\) and the third determines \(z'\); the first says \(\delta_1x=0\). Therefore \(x'\) is arbitrary and there are three free diagonal dimensions if \(x=0\), otherwise two. This gives \(r+3\) and \(r+2\), with the first pair of nontrivial multiplicities in the table. Reversing arrows exchanges \(r,x\) with \(s,y\), giving the next two rows.

If \(a=c\ne b\), put \(\alpha=a-b\), so \(b-c=-\alpha\). The first two equations yield \(x'=\alpha^{-1}\delta_1x\) and \(y'=-\alpha^{-1}\delta_2y\). The third becomes
\[
(\delta_1+\delta_2)(z+\alpha^{-1}x\otimes y)=0.
\]
Thus \(z'\) is arbitrary, and there are three or two free diagonal dimensions depending on whether \(z_*=0\) or not. For each \((x,y)\), translation \(z\mapsto z_*\) is bijective, giving \(q^{r+s}\) choices for each prescribed \(z_*\).

**All three diagonals equal.** Equation (1) simplifies to
\[
\delta_1x=0,\qquad\delta_2y=0,\qquad
(\delta_1+\delta_2)z=x\otimes y'-x'\otimes y.
\tag{2}
\]
If \(x=y=0\), the variables \(x',y',z'\) are free. The diagonal differences have dimension two if \(z=0\), otherwise one, producing centralizer dimensions \(D\) and \(D-1\).

If \(x\ne0\) and \(y=0\), the first equation forces \(\delta_1=0\) and the last is \(\delta_2z=x\otimes y'\). There is an extra free diagonal difference exactly when \(z\in x\otimes W\). If it exists, \(y'\) is uniquely determined for every \(\delta_2\); otherwise \(\delta_2=y'=0\). In either case \(x'\) and \(z'\) are free, giving dimensions \(h+r+2\) or \(h+r+1\). For fixed nonzero \(x\), the subspace \(x\otimes W\) has \(q^s\) elements. The symmetric argument with \(x=0\) and \(y\ne0\) gives the following two rows.

Finally, if \(x\ne0\) and \(y\ne0\), both diagonal differences vanish. The map \((x',y')\mapsto x\otimes y'-x'\otimes y\) has one-dimensional kernel: its solutions are exactly \((x',y')=(tx,ty)\) for \(t\in\mathbb F_q\). To see this, choose linear functionals nonzero on \(x\) and \(y\), respectively, and apply them to the tensor identity. The common diagonal scalar and the arbitrary \(z'\) contribute another \(1+h\) dimensions. Thus \(\dim C_A(u)=h+2\), independently of \(z\).

These cases partition all \(q^D\) algebra elements. Each table row counts its choices of diagonal and radical coordinates, so summing its monomials gives exactly \(H_{r,s,q}(T)\). For a centralizer of dimension \(c\), exactly \(q^c\) elements commute with its defining element. Summing these sizes proves the displayed commuting-pair and probability formulas. The numerical specializations follow by direct integer substitution into the table.

## Verification

The standalone `verify.py` enumerates every element in each specified small algebra, constructs the independent commutator linear map in the path basis, computes its rank by finite-field Gaussian elimination, and compares the resulting centralizer-dimension histogram with the table. The full exhaustive checks were performed at
\[
(q,r,s)=(2,1,1),(3,1,1),(4,1,1),(2,2,1),(2,1,2),(2,2,2),(3,2,1),(5,1,1),(4,2,1).
\]
The \(\mathbb F_4\) tests use the extension-field model \(\mathbb F_2[t]/(t^2+t+1)\). In particular, the in-scope \((2,2,2)\) case examines all \(2048\) elements. Every histogram agrees and the program prints `VERIFY_OK`. Each prediction is independently normalized by checking that its multiplicities sum to \(q^D\). The size-\(26\) examples were evaluated by exact rational arithmetic from the same symbolic table. These finite tests are checks, not proofs for arbitrary parameters.

## Relationship to prior work

Dutta, Basnet and Nath (arXiv:1510.08211v1, Sections 2–3) derive general bounds and isoclinism invariance for commuting probabilities of finite rings. Those results motivate centralizer counting, but do not give this specific two-parameter path-algebra centralizer spectrum. Their later paper arXiv:1803.04111v1 studies finite rings with prescribed *numbers of distinct element-centralizers*; this is different from the dimensions and multiplicities of centralizers for each element used here. Both full texts were examined.

The published result *Commutator fibers and commuting probabilities of finite Kronecker path algebras* handles a two-vertex one-arrow-family algebra whose radical squares to zero. The present three-vertex family has a nonzero tensor-product multiplication \(V\otimes W\subset J^2\), and neither its centralizer stratification nor the equal-dimension probability distinction follows by substituting arrow counts into the two-vertex theorem. The small special case \(r=s=1\) is the familiar algebra of upper-triangular \(3\times3\) matrices; it is tested here as a boundary check and is not the novelty claim. More generally, passing to the radical-square-zero quotient destroys the tensor-product term in (1), so formulas for that quotient cannot simply be transferred to \(A\).

## Limitations

No classification of the actual distinct centralizer subalgebras, beyond their dimensions and the number of defining elements, is claimed. The result does not cover arbitrary quivers with branching, loops, or imposed path relations. Searches and primary-text comparisons cannot rule out an older equivalent formula under different notation; independent bibliographic and mathematical audits have not been performed. The argument is self-contained and independent of small-field enumeration.

## References

1. J. Dutta, D. K. Basnet and R. K. Nath, *On commuting probability of finite rings*, arXiv:1510.08211v1, first submitted 28 October 2015; HTML full text at https://arxiv.org/html/1510.08211v1 (MSC 16U70, 16U80).
2. J. Dutta, D. K. Basnet and R. K. Nath, *Commuting probabilities of \(n\)-centralizer finite rings*, arXiv:1803.04111v1, first submitted 12 March 2018; HTML full text at https://arxiv.org/html/1803.04111v1.
3. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, publicly available RESULT.md at https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d/RESULT.md (two-vertex radical-square-zero case).
