# Four rank-five theories of nontrivial finite additive Steiner triple systems

## Finding

Let a Steiner triple system (STS) be a finite set of points with a collection of three-element blocks, with every pair of distinct points in exactly one block. Work in **the point-only relational language** with equality and one symmetric, irreflexive ternary block predicate \(B(x,y,z)\); no quasigroup function, named constants, or named blocks are present. An STS is *additive* if its points inject into an abelian group so that each block has sum zero. We consider nontrivial systems, of order greater than three.

For \(m\ge3\), write \(\mathcal P_m\) for the blocks \(\{a,b,a+b\}\) on the nonzero vectors of \(\mathbf F_2^m\). For \(d\ge2\), write \(\mathcal A_d\) for the blocks \(\{a,b,-a-b\}\) on \(\mathbf F_3^d\), with distinct points. By the additive-STS classification of Pavone (2014), these are precisely the nontrivial finite additive Steiner triple systems, up to isomorphism.

**Theorem.** The family has exactly four equivalence classes for first-order sentences of quantifier rank at most five:

| Class | Parameters | Smallest representative | Points |
| --- | --- | --- | ---: |
| Binary-small | \(\mathcal P_3\) | \(\mathcal P_3\) | 7 |
| Binary-stable | \(\mathcal P_m,\ m\ge4\) | \(\mathcal P_4\) | 15 |
| Ternary-small | \(\mathcal A_2\) | \(\mathcal A_2\) | 9 |
| Ternary-stable | \(\mathcal A_d,\ d\ge3\) | \(\mathcal A_3\) | 27 |

All nontrivial Steiner triple systems (additive or not) are equivalent through quantifier rank four in this language. Hence rank five is the **first depth** at which the four additive classes can separate. The sharp largest minimum representative size inside the additive family is \(27\).

Two rank-five sentences give all four signatures. For four variables, let \(C(a,b,c,d)\) assert pairwise distinctness and the absence of a block among every three of the four. For disjoint pairs abbreviate
\[
M(ab\mid cd):=\exists z\,[B(a,b,z)\land B(c,d,z)].
\]
These are abbreviations, not additional relation symbols. Define
\[
\Phi:=\exists a\exists b\exists c\exists d\,[C(a,b,c,d)\land M(ab\mid cd)\land M(ac\mid bd)]
\]
and
\[
\Psi:=\exists a\exists b\exists c\exists d\,[C(a,b,c,d)\land\neg M(ab\mid cd)\land\neg M(ac\mid bd)\land\neg M(ad\mid bc)].
\]
Every complete expansion of each formula has maximum quantifier nesting exactly five. The truth values \((\Phi,\Psi)\) are, respectively, \((1,0),(1,1),(0,0),(0,1)\) for the four classes listed above. Here \(\Phi\) expresses the existence of a six-point, four-block Pasch configuration, while \(\Psi\) expresses a four-point cap whose three opposite-pair completion coincidences are all absent.

## Assumptions and scope

The order-three STS is expressly excluded. All points in a block must be distinct. The words “quantifier rank” refer to maximum nested first-order quantifiers, not to the number of bound variables or the quantifier rank in a **functional** quasigroup language. The classification is for finite additive STSs, not arbitrary finite STSs at rank five. The universal rank-four agreement, used for sharpness, applies to all finite STSs of order at least seven.

## Proof

**(1) Uniform four-round theory of all nontrivial STSs.** Consider any tuple of three already selected points. If the tuple contains at most two distinct points, the only special fresh point is the unique completion of the distinct pair, if there is one; a further generic point exists because the STS has at least seven points. For three distinct selected points on a block, every selected pair is already completed by the third selected point, and every fresh fourth point has the same atomic block pattern. For three distinct selected points not on a block, the three selected-pair completions are distinct and outside the tuple: a coincidence between two completions of pairs sharing one point would violate uniqueness of pair completion. At least one other fresh point exists because there are at least seven points (three selected plus three completions consume only six). Thus the **entire one-point atomic extension spectrum of every selected triple** depends only on its equality-and-block atomic diagram, uniformly in every nontrivial STS. Descending through the recursive definitions of first-order types gives identical rank-one types of triples, rank-two types of pairs, rank-three types of singletons, and rank-four sentence theories. This proves all systems agree to rank four, including the four families here.

**(2) The binary stabilization.** Fix \(m,m'\ge4\). In a five-round Ehrenfeucht–Fraïssé game on \(\mathcal P_m,\mathcal P_{m'}\), preserve a linear isomorphism between the spans of all selected vectors through the first four rounds. Before the fourth choice there are at most three spanning vectors, so either a prescribed vector in the current span or a vector independent of it can always be matched because both ambient dimensions are at least four. For the fifth move, the atomic block relations involving that new point are completely determined by equality to previously selected points and by whether it equals one of the (at most six) pair sums of the four selected vectors. The maintained linear isomorphism matches these special points, including any repetitions. A generic fifth point exists on each side: the universe has at least fifteen points, while the forbidden union of four old points and six pair sums has at most ten points. Therefore the game is won, giving \(\mathcal P_m\equiv_5\mathcal P_{m'}\).

**(3) The ternary stabilization.** Fix \(d,d'\ge3\). During the first four rounds preserve an affine isomorphism between the affine spans of the selected tuples. Before the fourth choice, the affine span has dimension at most two, so all new affine-dependence possibilities can be matched in either space of dimension at least three. An affine map in characteristic three preserves the block law \(a+b+c=0\), because the translation contribution to the sum is three times the translation vector. On the fifth move, the only special fresh points are completions \(-a_i-a_j\) of pairs of previously chosen points; the affine isomorphism matches them. There are at most six such completions, and a generic point exists because \(3^d\ge27>10\). This gives \(\mathcal A_d\equiv_5\mathcal A_{d'}\).

**(4) The two independent separating bits.** The formula \(\Phi\) requires two different completion points for two opposite matchings of four distinct cap points, hence exactly the four blocks of a Pasch configuration on six distinct points. In any \(\mathcal P_m\), choose independent nonzero \(a,b,c\) and let \(d=a+b+c\), \(e=a+b\), \(f=a+c\); these six points witness \(\Phi\). In an affine \(\mathcal A_d\), the same four-block pattern would imply both \(a+b=c+d\) and \(a+c=b+d\). Subtraction gives \(2(b-c)=0\) over \(\mathbf F_3\), forcing \(b=c\), a contradiction. Thus \(\Phi\) exactly detects the binary family.

For \(\Psi\), consider a cap of four distinct binary vectors in \(\mathbf F_2^3\). Linear dependence and absence of a zero-sum triple force their four-vector sum to vanish. All three opposite-pair sums then coincide, so \(\Psi\) is false in \(\mathcal P_3\). Four independent vectors in \(\mathbf F_2^m\), \(m\ge4\), make \(\Psi\) true. In \(\mathcal A_2\), all six pair completions of a cap lie outside its four points, but the universe has only five other points. Two completions therefore coincide; their pairs must be disjoint by the STS uniqueness axiom. Thus \(\Psi\) is false in \(\mathcal A_2\). Four affinely independent points \(0,e_1,e_2,e_3\) in \(\mathbf F_3^d\), \(d\ge3\), have no collinear triple and no opposite-pair completion coincidence, making \(\Psi\) true.

The two truth-value bits distinguish all four cases, while (2) and (3) prove completeness within each case. By (1), the separation depth five is optimal. The smallest representative orders are forced by the allowable dimensions and verified separations, establishing the sharp bound of \(27\).

## Verification

The accompanying standalone standard-library Python program `verify.py` constructs the binary projective designs of vector dimensions three, four, and five and the ternary affine designs of dimensions two, three, and four. It checks exact Steiner pair coverage, computes the two formula bits (with direct finite enumeration where feasible and explicit algebraic certificates in the larger examples), and independently computes complete first-order Hintikka types from atomic diagrams for quantifier ranks zero through five. Its orbit reduction uses the kernels of every linear relation among selected binary vectors and of every affine-difference relation among selected ternary vectors; these classify the corresponding linear and affine automorphism orbits. Across the six tested structures the computed type signatures agree at ranks zero through four and split into precisely four signatures at rank five; both higher-dimensional pairs coincide. The recorded output appears in `verify_output.txt`.

The **universal dimension-stabilization assertions** are established by steps (2) and (3), not by extrapolation from the finite computations. The finite program is a reproducibility check, not independent external certification.

## Relationship to prior work

Ling–Colbourn–Grannell–Griggs (2000) and Grannell–Griggs–Whitehead (2000) study existence and construction of anti-Pasch Steiner triple systems. Pavone (2014) identifies the complete class of additive Steiner triple systems and discusses the algebraic Pasch/Veblen distinction; the present theorem uses his object classification but concerns **four exact depth-five first-order theories**, rather than algebraic isomorphism types or the occurrence of Pasch alone. Barbina–Casanovas (2019 arXiv version) study the model completion and infinite homogeneous Steiner quasigroups, not the finite bounded-rank additive subclasses. Heinlein–Östergård (2022) analyze algorithms and complexity for enumerating finite Pasch and other configurations, not the quantifier-rank partition. A previously recorded point-only rank-four classification of nontrivial Steiner designs supplies only the common lower-depth phenomenon; it does not imply these two separating formulas or the dimension-stability theorem at rank five.

## Limitations

No rank-six classification, no transfer to the functional Steiner-quasigroup language, and no rank-five classification for nonadditive STSs is asserted. The two historical anti-Pasch construction articles were available only at bibliographic/abstract level in this comparison. The complete 2014 mathematical text and relevant sections of the 2019 open preprint were inspected. An equivalent classification in unindexed or inaccessible work remains possible. The scientific review is self-review only, not independent validation.

## References

1. A. C. H. Ling, C. J. Colbourn, M. J. Grannell, T. S. Griggs, “Construction Techniques for Anti-Pasch Steiner Triple Systems,” *J. London Math. Soc.* 61 (2000), 641–657, DOI: `10.1112/S0024610700008838`; verified public issue date 2000-06-01.
2. M. J. Grannell, T. S. Griggs, C. A. Whitehead, “The resolution of the anti-Pasch conjecture,” *J. Combin. Designs* 8 (2000), 300–309, DOI: `10.1002/1520-6610(2000)8:4<300::AID-JCD7>3.0.CO;2-R`.
3. M. Pavone, “Additive Steiner triple systems,” *Bollettino di Matematica Pura ed Applicata* VII (2014), 9–15, institutional record: `https://hdl.handle.net/10447/104606`.
4. S. Barbina, E. Casanovas, “Model theory of Steiner triple systems,” arXiv:1805.06767, version of 2019-11-05 (published subsequently in *J. Mathematical Logic*).
5. D. Heinlein, P. R. J. Östergård, “Algorithms and complexity for counting configurations in Steiner triple systems,” *J. Combin. Designs* 30 (2022), 527–546, DOI: `10.1002/jcd.21839`.
