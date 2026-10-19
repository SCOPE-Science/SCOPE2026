# Valuation strata of prescribed Heisenberg commutators over finite chain rings

## Finding

**Theorem (complete prescribed-commutator distribution).** Let \(R\) be any finite commutative chain ring with maximal ideal \((\pi)\), residue field of cardinality \(q\), and ideal chain
\[R\supsetneq\pi R\supsetneq\cdots\supsetneq\pi^{n-1}R\supsetneq\pi^nR=0,\qquad n\ge2.\]
For every integer \(m\ge1\), form the Heisenberg group \(H_m(R)\) on triples \((x,y,z)\in R^m\times R^m\times R\), with product
\[(x,y,z)(x',y',z')=(x+x',y+y',z+z'+x\cdot y').\]
Use the group commutator convention \([g,h]=g^{-1}h^{-1}gh\). Let \(v(t)\) be the unique integer \(s\in\{0,\ldots,n-1\}\) such that \(t\in\pi^sR\setminus\pi^{s+1}R\), and set \(v(0)=n\). For \(t\in R\), write
\[F_m(t)=|\{(g,h)\in H_m(R)^2:[g,h]=(0,0,t)\}|.\]
Then
\[\boxed{F_m(t)=q^{2n}\left(\mathbf{1}_{\{t=0\}}q^{2mn}+\sum_{s=0}^{\min(v(t),n-1)}(q^{2m(n-s)}-q^{2m(n-s-1)})q^{(2m-1)n+s}\right).}\]
Every commutator is central and every central target is attained, so all other group elements have fiber size zero.

For every nonzero central target of valuation \(r\), the more explicit law is
\[\boxed{F_m(t)=q^{2n}(q^{2m}-1)q^{(4m-1)n-2m}\sum_{s=0}^{r}q^{-(2m-1)s},\quad 0\le r<n.}\]
These \(n\) fiber sizes are pairwise distinct, strictly increasing in \(r\); the size for valuation \(r\) occurs at exactly \(q^{n-r}-q^{n-r-1}\) nonidentity central targets. In particular the nonidentity-fiber spectrum has cardinality exactly \(n\), and the entire distribution depends only on \(q,n,m\), not on the isomorphism type of \(R\).

For \(R=\mathbb Z/4\mathbb Z\), \(q=2\), \(n=2\), \(m=1\), the central targets \(0,1,2,3\) have respectively \(1408,768,1152,768\) ordered-pair fibers. The identical counts hold for the nonisomorphic chain ring \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\).

## Assumptions and scope

The ring \(R\) is finite, commutative and has a linearly ordered ideal lattice; it need not have equal characteristic. The residue cardinality \(q\) is a prime power, \(n\ge2\), and \(m\ge1\). The result includes residue characteristic two. The cardinalities of the successive ideal layers are \(|\pi^sR|=q^{n-s}\) for \(0\le s\le n\). No division by two and no ring-field embedding are required. The theorem concerns exact ordered-pair fibers, not equivalence classes of pairs. The usual finite-field case \(n=1\) follows from the same formula but is not part of the novelty claim.

## Proof

**1. The commutator and its support.** The inverse of \((x,y,z)\) is \((-x,-y,-z+x\cdot y)\). A direct multiplication gives
\[[ (x,y,z),(x',y',z') ]=(0,0,x\cdot y'-x'\cdot y).\]
Thus every commutator belongs to the central copy of \((R,+)\). Conversely, setting the first coordinate of \(x\) equal to one and the first coordinate of \(y'\) equal to any prescribed \(t\in R\), and setting all other horizontal coordinates to zero, realizes \((0,0,t)\). A nonzero horizontal coordinate can likewise be detected by a complementary coordinate of another element, so the center and derived subgroup both equal \(\{(0,0,t):t\in R\}\).

**2. The image of each horizontal commutator functional.** For a fixed horizontal vector \(a=(x,y)\in R^{2m}\), consider the \(R\)-linear functional
\[L_a:R^{2m}\longrightarrow R,\qquad L_a(x',y')=x\cdot y'-x'\cdot y.\]
If \(a\neq0\), let \(s\) be the minimum of the valuations of its \(2m\) coordinates. All coefficients of \(L_a\) lie in \(\pi^sR\), so \(\operatorname{im}(L_a)\subseteq\pi^sR\). At least one coordinate of \(a\) is a unit multiple of \(\pi^s\); choosing its complementary input coordinate to be one shows that \(\pi^sR\subseteq\operatorname{im}(L_a)\). Hence
\[\operatorname{im}(L_a)=\pi^sR,\qquad |\ker L_a|=\frac{q^{2mn}}{q^{n-s}}=q^{(2m-1)n+s}.\]
Every target \(t\in\pi^sR\) therefore has exactly \(q^{(2m-1)n+s}\) horizontal preimages, and every target outside this ideal has none. If \(a=0\), the functional is zero and its zero-target fiber is the full set of \(q^{2mn}\) input vectors.

**3. Number of vectors in each valuation stratum.** A horizontal vector has minimum-coordinate valuation at least \(s\) exactly when it lies in \((\pi^sR)^{2m}\), a set of cardinality \(q^{2m(n-s)}\). Subtracting the next stratum shows that the number with minimum valuation exactly \(s<n\) is
\[A_s=q^{2m(n-s)}-q^{2m(n-s-1)}.\]
For a fixed target \(t\) the contributing nonzero horizontal vectors are precisely those with \(s\le v(t)\). Summing their preimage counts, and adding the \(a=0\) contribution only for \(t=0\), gives the horizontal count within the parentheses of the theorem. The independent central coordinates \(z,z'\in R\) contribute the factor \(q^{2n}\). This proves the first boxed identity, including the zero target.

**4. Geometric law, distinctness and multiplicities.** For \(t\neq0\) with \(r=v(t)\), factor \(A_s=(q^{2m}-1)q^{2m(n-s-1)}\) inside the sum and combine exponents to obtain the second boxed identity. Successive values differ by
\[F_{m,r}-F_{m,r-1}=q^{2n}A_rq^{(2m-1)n+r}>0,\qquad 1\le r<n,\]
and \(F_{m,0}>0\). The number of elements \(t\in\pi^rR\setminus\pi^{r+1}R\) is \(q^{n-r}-q^{n-r-1}\), proving the exact multiplicity distribution and that all \(n\) sizes occur. Every expression uses only \(q,n,m\), which proves ring-universality.

**5. Total-count consistency.** Summing horizontal fibers over all \(t\in R\) counts each ordered pair of horizontal vectors once. Alternatively, a nonzero horizontal vector of minimum valuation \(s\) has \(q^{n-s}\) available targets and \(q^{(2m-1)n+s}\) preimages per target, giving \(q^{2mn}\) input vectors. The zero horizontal vector also has \(q^{2mn}\) inputs. Consequently \(\sum_{t\in R}F_m(t)=|H_m(R)|^2=q^{(4m+2)n}\), as required.

## Verification

The self-contained standard-library program `checker.py` performs exact finite-ring enumerations. It independently constructs the multiplication and additive structure for several modular rings, for \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\), and for \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\). It counts all horizontal symplectic-form values and compares every target separately with the theorem. For three small rings it also evaluates the group commutator as a four-factor group word, including central coordinates, without invoking the formula in that part of the check. It prints `VERIFY_OK` on success.

Verified sample horizontal fiber vectors, listed by target valuation and followed by the zero target, are \((48,72,88)\) for \(q=2,n=2,m=1\), \((384,576,672,736)\) for \(q=2,n=3,m=1\), and \((3840,4800,5056)\) for \(q=4,n=2,m=1\). Finite checks are diagnostic; the proof above covers all finite commutative chain rings and all positive ranks.

## Relationship to prior work

Diaconis and Malliaris (2021, arXiv:2107.02923, §§1–2.1) describe the higher Heisenberg groups over prime finite fields and their commuting graphs, and give the zero-commutator pair count in that setting. Their field assumption corresponds to ring length one; the present theorem identifies every prescribed nonzero commutator fiber over chain rings of all lengths at least two.

Nath and Yadav (2012 preprint, arXiv:1212.4306, §§1–3) study prescribed-commutator probabilities for groups with two conjugacy class sizes, including Camina class-two groups. Naik (2018, arXiv:1805.00091, Theorems 1.3 and 1.4 and §3) constructs class-two groups with arbitrarily many nonidentity fiber sizes while retaining only two conjugacy class sizes. These are important precedents for the fiber-spectrum question, but they do not supply the present chain-ring valuation law: for \(n\ge2\), \(H_m(R)\) itself has \(n+1\) conjugacy class sizes \(1,q,\ldots,q^n\).

The general finite-group fiber formula in Nath–Yadav, Lemma 3.1, can be applied to any group given sufficient centralizer information; the new content here is the explicit uniform evaluation for every target and every \(m,q,n\), together with strict valuation stratification and ring-independence. The general existence statement that arbitrarily many fiber sizes may occur is not asserted as new.

## Limitations

The theorem does not classify the groups \(H_m(R)\) up to isomorphism and does not address non-chain local rings, noncommutative rings, or polynomial words other than the single commutator. The originality claim is limited to the natural chain-ring family with \(n\ge2\) and its exact valuation-resolved counts. General character formulas and further literature on commutator word maps might imply this specialized formula after additional evaluation; that possibility is not ruled out merely by search. No independent audit or external mathematical certification has been performed.

## References

- Persi Diaconis and Maryanthe Malliaris, *Complexity and randomness in the Heisenberg groups (and beyond)*, arXiv:2107.02923, first publicly submitted 2021-07-06, https://arxiv.org/abs/2107.02923 .
- Rajat K. Nath and Manoj K. Yadav, *Probability that a given element of a group is a commutator of any two randomly chosen group elements*, arXiv:1212.4306, 2012, https://arxiv.org/abs/1212.4306 .
- Tushar Kanta Naik, *On the probability distribution associated to commutator word map in finite groups II*, arXiv:1805.00091, 2018, https://arxiv.org/abs/1805.00091 .
- Jon Cocke and Meng-Che Ho, *The Probability Distribution of Word Maps on Finite Groups*, arXiv:1807.07111, 2018, https://arxiv.org/abs/1807.07111 .
