# The four-point nonlattice threshold for BLAL implications

## Finding

Let \(C_n=\{0,1,\ldots,n-1\}\) carry the standard bounded-chain operations \(\wedge=\min\), \(\vee=\max\), bottom \(0\) and top \(n-1\). Let \(\mathcal I_n\) consist of **all** binary operations \(\Rightarrow:C_n^2\to C_n\) for which the expanded algebra satisfies equations (E1)–(E11) and quasi-equations (QE1)–(QE3) of Cornejo–Esteva–Fariñas del Cerro–Godo–Medina (2026), Theorem 16. Order \(\mathcal I_n\) pointwise. Then

\[
(|\mathcal I_1|,|\mathcal I_2|,|\mathcal I_3|,|\mathcal I_4|)=(1,1,4,25).
\]

For \(n\leq3\), these posets are chains and hence lattices. The poset \(\mathcal I_4\) is **not** a lattice: it has a pair with no join and a pair with no meet. Thus four is the sharp smallest bounded-chain cardinality at which the pointwise order on BLAL implications fails to be a lattice.

## Assumptions and scope

The class is the full equivalent algebraic semantics \(\mathrm{BLAL}\) defined in the cited Theorem 16, **not** the subclass of Heyting residua, adjoint pairs, or an additional semilinear logic's extra equations. The fixed carrier is a labelled bounded chain; pointwise ordering of the implication tables is not logical-entailment ordering. The result is a finite statement for \(1\leq n\leq4\), not a claim about all larger \(n\).

The axioms checked by the supplied verifier have the following complete form. Every expression in this paragraph is required to equal the top element:

\[
\begin{aligned}
\mathrm{E1}:&(x\wedge y)\Rightarrow x, &\mathrm{E2}:&(x\wedge y)\Rightarrow y,\\
\mathrm{E3}:&(z\Rightarrow x)\Rightarrow((z\Rightarrow y)\Rightarrow(z\Rightarrow(x\wedge y))),\\
\mathrm{E4}:&x\Rightarrow(x\vee y), &\mathrm{E5}:&y\Rightarrow(x\vee y),\\
\mathrm{E6}:&(x\Rightarrow z)\Rightarrow((y\Rightarrow z)\Rightarrow((x\vee y)\Rightarrow z)),\\
\mathrm{E7}:&x\Rightarrow x,\\
\mathrm{E8}:&(x\Rightarrow y)\Rightarrow((y\Rightarrow z)\Rightarrow(x\Rightarrow z)),\\
\mathrm{E9}:&(y\Rightarrow z)\Rightarrow((x\Rightarrow y)\Rightarrow(x\Rightarrow z)),\\
\mathrm{E10}:&0\Rightarrow x, &\mathrm{E11}:&x\Rightarrow(0\Rightarrow0).
\end{aligned}
\]

The three quasi-equations are: QE1: if \(x\) is top and \(x\Rightarrow y\) is top, then \(y\) is top; QE2: if \(x\) is top then \((x\Rightarrow x)\Rightarrow x\) is top; QE3: if \(x\Rightarrow y\) and \(y\Rightarrow x\) are top, then \(x=y\). These are required for every valuation of the variables in the chain.

## Proof

**Order lemma.** In every BLAL algebra, \(x\Rightarrow y\) equals top exactly when \(x\leq y\) in the lattice order (Cornejo et al., Proposition 21). This is not a freely added property. For completeness: E1 makes \((x\wedge y)\Rightarrow y\) top. Conversely, from \(x\Rightarrow y\) top, apply E7 and E3 with \(z=x\), and then QE1 twice, to obtain \(x\Rightarrow(x\wedge y)\) top. E1 also gives \((x\wedge y)\Rightarrow x\) top; QE3 then forces \(x=x\wedge y\). This proves the equivalence.

**Exhaustive search is finite.** Consequently every table has value \(n-1\) whenever \(x\leq y\), and each of the \(n(n-1)/2\) strict-lower-triangle entries lies in \(\{0,\ldots,n-2\}\). There are exactly \((n-1)^{n(n-1)/2}\) such candidate tables, with the empty product interpreted as one. Checking the displayed identities and quasi-equations at **all** triples \((x,y,z)\in C_n^3\) gives the counts \(1,1,4,25\) for \(n=1,2,3,4\). The complete verifier in `checker.py` does precisely this; no statistical sampling or unproved pruning is involved.

For \(n=3\), encode the lower triangle in the order \(((1,0),(2,0),(2,1))\). The four admissible tuples, **exhaustively**, are

\[
(0,0,0)<(0,0,1)<(1,0,1)<(1,1,1),
\]

where the displayed comparison is pointwise. The \(n=1,2\) cases are singletons. Therefore every \(\mathcal I_n\) for \(n\leq3\) is a lattice.

**Explicit nonlattice witness.** For \(n=4\), encode the strict lower triangle in the fixed order

\[
((1,0),(2,0),(2,1),(3,0),(3,1),(3,2)).
\]

The following four tuples each satisfy every BLAL axiom, as checked exhaustively by `checker.py`:

\[
\begin{aligned}
A&=(1,1,1,1,1,2),&B&=(2,1,1,0,1,2),\\
C&=(1,0,1,0,1,2),&D&=(1,1,1,0,1,1).
\end{aligned}
\]

They satisfy \(C,D\leq A,B\) pointwise and have matching coordinatewise infimum/supremum

\[
\min(A,B)=\max(C,D)=M=(1,1,1,0,1,2).
\]

But \(M\notin\mathcal I_4\). Indeed, at \((x,y,z)=(3,2,0)\), its E8 term evaluates to

\[
(3\Rightarrow2)\Rightarrow((2\Rightarrow0)\Rightarrow(3\Rightarrow0))
=2\Rightarrow(1\Rightarrow0)=2\Rightarrow1=1\neq3.
\]

If the join \(C\vee D\) existed in the pointwise poset, it would dominate \(C,D\), hence dominate their coordinatewise maximum \(M\); because \(A,B\) are upper bounds, that join would also be below their coordinatewise minimum \(M\), forcing it to equal the inadmissible table \(M\). Contradiction. Dually, any meet of \(A,B\) would lie above both \(C,D\) and below both \(A,B\), forcing the same impossible table \(M\). Hence there is neither the indicated join nor the indicated meet, and the threshold is sharp.

## Verification

Execute `python3 checker.py` using Python 3 standard library. The verifier implements all 11 identities and all 3 quasi-equations exactly as stated, fills the permitted truth tables, tests **every** triple for each candidate, asserts the counts and three-element order, and evaluates the four admissible witnesses and excluded middle table. Its expected successful terminal output starts with `ALL_CHECKS_OK counts=(1,1,4,25) candidates=(1,1,8,729)` and ends with `No join of C,D and no meet of A,B`.

The checked candidate counts for \(n=1,2,3,4\) are \(1,1,8,729\). Thus this is an exhaustive small-carrier classification, not an extrapolation to arbitrary chain length. The short order-theoretic contradiction, not enumeration alone, proves failure of joins and meets once the listed tables have been verified.

## Relationship to prior work

Cornejo et al. (2026), Theorem 16, **define** the relevant quasivariety and its complete axiomatization; Proposition 21 proves the order lemma used here. Their Example 22 exhibits an implication that is monotone and order-reflecting but fails the BLAL axioms. The present claim is solely the exact small-chain census and pointwise nonlattice threshold, not those earlier algebraizability or order results.

Cornejo, Medina and Ramírez-Poussa (2021), Section 5, prove complete-lattice structure for classes of **adjoint implication pairs and triples**. Their operators satisfy residuation/Galois conditions not imposed in the broader BLAL quasivariety. Their positive lattice result therefore does not imply a lattice structure for all BLAL implications; the explicit four-element witness proves the distinction is substantive. Broader lattice/order and Rasiowa-implication terminology were considered in the literature comparison.

## Limitations

The four cardinalities and nonlattice threshold hold for chains with at most four elements. No formula is proposed for arbitrary \(n\), and no assertion is made about other partial orders or other algebraic signatures. The enumeration algorithm is an executable exhaustive certificate for the finite claims; it does not establish a theorem about an unbounded family. Historical priority against every possible synonymous classification of implications is not conclusively established by a finite literature search. Independent audit has not been performed.

## References

1. M. E. Cornejo, F. Esteva, L. Fariñas del Cerro, L. Godo and J. Medina, *Bounded and multi-adjoint lattice algebraizable logics*, International Journal of Approximate Reasoning **195** (2026), 109682, DOI: `10.1016/j.ijar.2026.109682`. Original open-access author PDF: https://www.iiia.csic.es/media/filer_public/57/05/5705341f-628e-4395-9756-0e02ba2865f2/cornejo-esteva-farinas-godo-medina-ijar26.pdf . Available online 7 April 2026. Theorem 16, Proposition 21, Example 22.
2. M. E. Cornejo, J. Medina and E. Ramírez-Poussa, *Algebraic structure and characterization of adjoint triples*, Fuzzy Sets and Systems (2021), DOI: `10.1016/j.fss.2021.02.002`, especially Section 5 and Corollary 31. Author manuscript: https://rodin.uca.es/bitstream/handle/10498/30935/AlgebraicStructure_GIP_AT_R2_301220.pdf?isAllowed=y&sequence=1 .
