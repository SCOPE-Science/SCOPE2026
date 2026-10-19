# Complete radical-multiplication Jordan spectra of the four-generator exterior algebra

## Finding
Let \(k=\mathbb F_q\), let \(V=k^4\), and put \(E=\bigwedge_k V\) with radical \(J=\bigoplus_{i=1}^4\bigwedge^i V\). For every \(a\in J\), write \(L_a:E\to E\) for left multiplication by \(a\). Then the entire Jordan partition of \(L_a\) belongs to the following explicit list. The table gives the exact number of elements realizing each partition, for every prime power \(q\).

For **odd** \(q\):

| Jordan partition of \(L_a\) | Exact multiplicity |
|---|---:|
| \((3^2,2^4,1^2)\) | \((q^4-1)(q^6-q^3)q^5\) |
| \((2^8)\) | \((q^4-1)q^8\) |
| \((3,2^4,1^5)\) | \(q^7(q-1)(q^3-1)\) |
| \((2^4,1^8)\) | \(q^5(q^2+1)(q^3-1)\) |
| \((2^2,1^{12})\) | \(q(q^4-1)\) |
| \((2,1^{14})\) | \(q-1\) |
| \((1^{16})\) | \(1\) |

For **even** \(q\):

| Jordan partition of \(L_a\) | Exact multiplicity |
|---|---:|
| \((2^8)\) | \((q^4-1)q^{11}\) |
| \((2^6,1^4)\) | \(q^7(q-1)(q^3-1)\) |
| \((2^4,1^8)\) | \(q^5(q^2+1)(q^3-1)\) |
| \((2^2,1^{12})\) | \(q(q^4-1)\) |
| \((2,1^{14})\) | \(q-1\) |
| \((1^{16})\) | \(1\) |

In both characteristics, these mutually exclusive multiplicities sum exactly to \(q^{15}=|J|\). In odd characteristic, precisely \((q^4-1)(q^6-q^3)q^5\) elements have nilpotency index three and two size-three blocks, and precisely \(q^7(q-1)(q^3-1)\) have one size-three block. In even characteristic, every element of \(J\) squares to zero.

## Assumptions and scope
The exterior algebra is unital and associative, with its usual graded-anticommutative multiplication in every characteristic. Here \(\bigwedge^i V\) means the homogeneous exterior degree, \(\operatorname{rank}(\omega)=2\) or \(4\) for a two-form refers to its alternating-form rank, and a partition such as \((3^2,2^4,1^2)\) denotes two blocks of length three, four of length two, and two of length one. We classify left multiplication on the full regular module \(E\), **not** an automorphism orbit or the adjoint/commutator map.

Every radical element has a unique decomposition \(a=\ell+\omega+\eta+\theta\), with exterior degrees one, two, three, four, respectively. The strata behind the tables are as follows. For odd \(q\), a nonzero \(\ell\) gives partition \((3^2,2^4,1^2)\) exactly when \(\ell\wedge\omega\ne0\), and \((2^8)\) otherwise. For even \(q\), every nonzero \(\ell\) gives \((2^8)\). If \(\ell=0\) and \(\omega\ne0\), two-form rank four gives \((3,2^4,1^5)\) in odd characteristic or \((2^6,1^4)\) in even characteristic, whereas two-form rank two gives \((2^4,1^8)\) in both. When \(\ell=\omega=0\), successive leading exterior degrees three, four and zero give the final three rows.

## Proof
**Step 1: the case of nonzero linear part.** Suppose \(\ell\ne0\). Choose a basis with \(\ell=e_1\), put \(W=\operatorname{span}(e_2,e_3,e_4)\), and write \(B=\bigwedge W\), so \(E=B\oplus e_1 B\) with \(\dim_k B=8\). There are unique \(v\in B\), with constant term one and hence invertible, and \(c\in\bigwedge^{\ge2}W\) such that \(a=e_1v+c\). Right multiplication by \(v^{-1}\) is invertible on \(E\) and does not change the image of \(L_a\), because \(av^{-1}E=aE\). Thus \(\operatorname{rank}(L_a)=\operatorname{rank}(L_{a'})\) for \(a'=e_1+u+w\), where \(u\in\bigwedge^2W\) and \(w\in\bigwedge^3 W\).

For each \(b\in B\), the vector \(a'b=e_1b+(u+w)b\) belongs to \(a'E\). The eight such vectors are linearly independent by their \(e_1B\)-components. Conversely, using \(e_1 u=u e_1\), \(e_1w=-w e_1\), and \((u+w)(u-w)=0\) (every constituent has exterior degree at least four in the three-dimensional space \(W\)), we obtain, for each \(b\in B\),
\[
a'e_1b=e_1(u-w)b=a'((u-w)b).\]
Therefore \(a'E\) is precisely the eight-dimensional span of \(a'B\), and \(\operatorname{rank}(L_a)=8\), over any field.

**Step 2: squares and their ranks.** For arbitrary \(a=\ell+\omega+\eta+\theta\) the exterior-degree rule gives
\[a^2=2\ell\wedge\omega+\omega\wedge\omega.\]
Indeed, odd-degree homogeneous terms square to zero, cross products of odd and even degrees cancel unless the degrees exceed four (and every degree at least five vanishes). When \(\operatorname{char}k=2\), every \(a\in J\) satisfies \(a^2=0\). In odd characteristic, if \(\ell\ne0\) and \(\ell\wedge\omega\ne0\), then multiplication by \(a^2\) has rank two: a nonzero three-form contributes its image on \(1\) and a nonzero top-degree image on a one-dimensional quotient of \(V\); a possible four-form summand changes neither rank. If \(\ell\wedge\omega=0\), then \(\omega=\ell\wedge z\) for some \(z\in V\), whence \(\omega^2=0\) and \(a^2=0\).

If \(\ell=0\), then \(a^2=\omega^2\), a top-degree form. A nonzero alternating two-form on a four-space has rank either two or four; \(\omega\wedge\omega\) vanishes for rank two, while in odd characteristic it is twice the Pfaffian times the volume form and is nonzero precisely for rank four. Hence \(\operatorname{rank}(L_a^2)\) is either zero or one as specified by the tables. The identities also give \(a^3=0\) in all characteristics.

**Step 3: the case of vanishing linear part.** Assume \(\ell=0\), \(\omega\ne0\). The element \(a\cdot1\) has a nonzero degree-two leading term and contributes one independent image vector. The vectors \(a\cdot V\) have degree-three leading components \(\omega\wedge V\); their dimension modulo top degree is \(d=\operatorname{rank}(V\xrightarrow{\omega\wedge-}\bigwedge^3 V)\). Finally, \(a\bigwedge^2V=\omega\wedge\bigwedge^2V\) spans the degree-four line; it also absorbs the possible degree-four contributions of \(\eta\wedge V\). Thus \(\operatorname{rank}(L_a)=2+d\). The map \(\omega\wedge-\) on \(V\) has rank \(d=2\) for two-form rank two, and rank \(d=4\) for two-form rank four. The corresponding multiplication ranks are four and six. When \(\ell=\omega=0\), a nonzero degree-three term produces exactly a two-dimensional image (degree three on \(1\), degree four on \(V\)); a pure nonzero degree-four term produces rank one, and zero produces rank zero.

**Step 4: Jordan partitions.** Every \(L_a\) is nilpotent with \(L_a^3=0\). Put \(r_1=\operatorname{rank}(L_a)\), \(r_2=\operatorname{rank}(L_a^2)\). The numbers of Jordan blocks of sizes three, two and one are respectively
\[b_3=r_2,\qquad b_2=r_1-2r_2,\qquad b_1=16-2r_1+r_2.\]
Substitution of the ranks just proved yields exactly the listed partitions.

**Step 5: exact field counts.** For a fixed nonzero \(\ell\), the linear wedge map \(\ell\wedge-:\bigwedge^2V\to\bigwedge^3V\) has a three-dimensional kernel, so exactly \(q^3\) of the \(q^6\) possible two-forms obey \(\ell\wedge\omega=0\). There are \(q^4-1\) choices for \(\ell\) and independently \(q^5\) choices for the degree-three and degree-four parts. Therefore the odd-characteristic nonzero-linear counts are \((q^4-1)(q^6-q^3)q^5\) and \((q^4-1)q^8\); in even characteristic they merge into \((q^4-1)q^{11}\).

Among all nonzero two-forms on a four-space, the number of decomposable/rank-two forms is
\[(q-1)\genfrac{[}{]}{0pt}{}{4}{2}_q=(q^2+1)(q^3-1).\]
The remaining rank-four forms number
\[q^6-1-(q^2+1)(q^3-1)=q^2(q-1)(q^3-1).\]
These identities follow either from the Gaussian binomial coefficient for two-planes or from the full-rank skew-form orbit \(\operatorname{GL}_4(q)/\operatorname{Sp}_4(q)\). When \(\ell=0\), each two-form has \(q^5\) extensions by \(\eta+\theta\), yielding the middle rows. Finally, with \(\ell=\omega=0\), there are \((q^4-1)q\) ways to choose a nonzero three-form and arbitrary four-form, \(q-1\) ways to choose a pure nonzero four-form, and one zero element. The totals are exactly \(q^{15}\), completing the classification.

## Verification
The included \(\texttt{artifacts/verify.py}\) implements the sixteen-dimensional exterior multiplication independently by bitmask signs, constructs \(L_a\) and \(L_{a^2}\), computes exact finite-field matrix ranks, and compares against the degree/Pfaffian stratification. Its recorded outputs include exhaustive enumeration of all \(2^{15}=32768\) binary radical elements by independent structural classification; for all \(p^6\) pure two-forms over \(p=2,3,5\), it **directly** checks both multiplication ranks using matrix Gaussian elimination. Additional fully independent multiplication-rank checks use 8,000 randomly chosen elements over \(\mathbb F_2\) and 1,500 each over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\). It prints \(\texttt{VERIFY_OK_EXTERIOR_JORDAN}\) on success. These finite checks corroborate but cannot prove the formulas for every prime power; that extension is supplied by the field-uniform proof.

## Relationship to prior work
Exterior multiplication, Pfaffian stratification of two-forms on a four-space, and enumeration of alternating-form ranks are classical ingredients, not claimed as new. Fløystad's 2004 paper studies resolutions over exterior algebras and Grassmannian constructions; its Theorems 2.1 and 5.1 are about complexes/Tate resolutions rather than the complete finite-field histogram of Jordan partitions for arbitrary positive-degree multipliers. Carlson–Friedlander–Pevtsova's work on constant Jordan type studies restriction along rank-one elementary-subgroup operators; Benson–Pevtsova's realization theorem uses exterior algebra in a cohomological construction. Neither establishes this all-radical finite-field distribution. Work on Jordan types of Artinian algebras over infinite fields treats different families and questions; linear-form or generic Jordan information alone is insufficient to infer all the inhomogeneous strata here. The finding is the **combined complete stratification and multiplicity formulas** across odd and even finite fields, not any one classical component of the proof.

## Limitations
The result concerns the exterior algebra on exactly four generators and its regular left module. It does not classify similarity under algebra automorphisms, Jordan types on other modules, group-theoretic orbit counts, or exterior algebras on more generators. Computational tests used prime fields and finite samples except for the explicitly exhaustive binary and two-form strata; arbitrary extension fields rely on the proof. Existing results on exterior products and Pfaffian orbits mean literature priority requires further independent bibliographic examination; no independent scientific audit has been performed.

## References
1. G. Fløystad, “Exterior algebra resolutions arising from homogeneous bundles,” *Math. Scand.* **94** (2004), 191–201; DOI: 10.7146/math.scand.a-14438. First publicly dated journal source: 2004-06-01. Full article: https://journals.msp.org/mscand/article/download/781/780/812.
2. J. F. Carlson, E. M. Friedlander and J. Pevtsova, “Modules of Constant Jordan Type,” *J. Reine Angew. Math.* **614** (2008), 191–234; preprint publicly circulated 2007. The actual paper concerns modules for finite group schemes and elementary abelian subgroups.
3. D. J. Benson and J. Pevtsova, “A realization theorem for modules of constant Jordan type and vector bundles,” arXiv:1007.3827v1 (2010-07-22).
4. A. Iarrobino, P. Macias Marques and C. McDaniel, “Free extensions and Jordan type,” arXiv:1806.02767 (2018). Cited for broader Jordan-type context, not an archive-date anchor.
