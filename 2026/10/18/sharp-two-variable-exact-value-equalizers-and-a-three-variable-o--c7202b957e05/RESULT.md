# Sharp two-variable exact-value equalizers and a three-variable obstruction in FOUR

## Finding
Let \(\mathbf{FOUR}=\{N,T,F,B\}\) carry Belnap–Dunn's truth operations \(\wedge,\vee,\neg\). For \(k\ge 1\), consider constant-free formulas \(\varphi,\psi\) in exactly the available variables \(p_1,\ldots,p_k\), allowing some variables not to occur, and write
\[
E(\varphi,\psi)=\{a\in\mathbf{FOUR}^k:\varphi(a)=\psi(a)\}.
\]
Encode a value by truth/falsity bits \((t,f)\in\{0,1\}^2\), with \(N=(0,0)\), \(T=(1,0)\), \(F=(0,1)\), \(B=(1,1)\). Give \(\{0,1\}^{2k}\) the coordinatewise order, and let the order-reversing involution \(\theta\) replace each bit pair \((t,f)\) by \((1-f,1-t)\). This interchanges \(N\) with \(B\) and fixes \(T,F\).

**General characterization.** A subset \(E\subseteq\mathbf{FOUR}^k\) is an exact-value equality locus of two such formulas if and only if there exists an order-convex set \(D\subseteq\{0,1\}^{2k}\), containing neither the bottom nor the top point, such that
\[
E=\{0,1\}^{2k}\setminus\bigl(D\cup\theta(D)\bigr).
\]
In particular, every equality locus is invariant under \(\theta\) and contains the all-\(N\) and all-\(B\) assignments.

**Sharp first obstruction.** For \(k=1,2\), these last two elementary conditions are also sufficient. There are exactly \(4\) equality loci for one variable and exactly \(512\) for two. Starting at \(k=3\), invariance and inclusion of both extreme assignments no longer suffice. Thus three variables are the first arity at which an additional convexity obstruction appears.

In two variables there are exactly \(166\) distinct term operations, hence \(27{,}556\) ordered term-operation pairs. Their exact equality-cardinality histogram is:

| Equal assignments | Ordered pairs | Distinct equality loci |
| ---: | ---: | ---: |
| 2 | 238 | 1 |
| 3 | 240 | 4 |
| 4 | 644 | 11 |
| 5 | 1,056 | 24 |
| 6 | 1,668 | 41 |
| 7 | 2,416 | 60 |
| 8 | 3,240 | 75 |
| 9 | 3,808 | 80 |
| 10 | 4,072 | 75 |
| 11 | 3,696 | 60 |
| 12 | 2,976 | 41 |
| 13 | 1,920 | 24 |
| 14 | 1,016 | 11 |
| 15 | 400 | 4 |
| 16 | 166 | 1 |
| **Total** | **27,556** | **512** |

Thus every probability \(j/16\), for \(2\le j\le16\), occurs as the exact-value agreement frequency of two formulas with two uniformly distributed FOUR-valued variables.

## Assumptions and scope
All formula equalities compare **full four-valued outputs**, not merely designatedness or their truth bits. No constants, implications, modalities, semantic restrictions on valuations, or additional connectives are allowed. All \(4^k\) valuations are present; the two-variable histogram counts **ordered pairs of distinct term operations as functions**, with identical pairs included, and not formula strings. Order-convexity means: if \(a,c\in D\) and \(a\le b\le c\), then \(b\in D\).

## Proof
**1. Truth-bit normal form.** For a formula \(\varphi\), let \(f_\varphi\colon\{0,1\}^{2k}\to\{0,1\}\) be its truth bit. Directly from the FOUR truth tables,
\[
(t,f)(\varphi\wedge\psi)=(t_\varphi\wedge t_\psi,\ f_\varphi\vee f_\psi),\qquad
(t,f)(\varphi\vee\psi)=(t_\varphi\vee t_\psi,\ f_\varphi\wedge f_\psi),
\]
where \(\neg\) swaps truth and falsity bits. By induction on formulas, \(f_\varphi\) is a nonconstant monotone Boolean function of the \(2k\) bit coordinates, with \(f_\varphi(\mathbf0)=0\) and \(f_\varphi(\mathbf1)=1\); the falsity bit is exactly \(1-f_\varphi(\theta x)\). Conversely, any monotone Boolean \(f\) with those endpoint values is a constant-free positive disjunction of nonempty conjunctions of the literal truth bits \(t_i,f_i\). Replacing these bits by \(p_i,\neg p_i\) gives a FOUR formula with truth bit \(f\) and falsity bit \(1-f\circ\theta\). No nullary connectives are needed; for instance \(f\equiv0,1\) are excluded by the required endpoints.

**2. Boolean disagreements.** For two monotone endpoint-preserving Boolean functions \(f,g\), put \(D=\{x:f(x)\ne g(x)\}\). If \(a\le b\le c\) with \(a,c\in D\), then the pair \((f(a),g(a))\) and the pair \((f(c),g(c))\) must have identical orientations: if their orientations differed, coordinatewise monotonicity of both functions would be violated. Both endpoints therefore force the same unequal orientation at the intermediate \(b\); hence \(b\in D\). Thus \(D\) is order-convex and excludes both cube endpoints.

Conversely, suppose \(D\) is a nonempty convex subset avoiding the endpoints. Define \(U=\uparrow D\). Convexity makes \(U\setminus D\) an upset: if \(x\in U\setminus D\), \(y\ge x\), and \(y\in D\), then some \(d\in D\) has \(d\le x\le y\), forcing \(x\in D\), contradiction. The Boolean functions \(\mathbf1_U\) and \(\mathbf1_{U\setminus D}\) are monotone, endpoint-preserving, and differ **exactly** on \(D\). For empty \(D\), take the same nonconstant projection twice. Both Boolean functions can be translated to FOUR formulas by Step 1.

**3. FOUR equalizers.** Equality of both truth and falsity bits for the formulas represented by \(f,g\) at \(x\) is equivalent to \(f(x)=g(x)\) and \(f(\theta x)=g(\theta x)\). Therefore its complement is \(D\cup\theta D\). Step 2 proves necessity and sufficiency of the stated general characterization.

**4. Exact low-arity classification.** For \(k=1\) the Boolean truth-bit functions have \(2\) inputs and there are \(4\) nonconstant monotone functions. For \(k=2\) they have \(4\) inputs and there are exactly \(166\) nonconstant monotone functions, the Dedekind number \(168\) minus the two constant functions. The accompanying complete verifier tests each such function by its full truth table, all \(166^2\) ordered pairs, and all order-convex subsets of the four-bit cube excluding its two endpoints. Independently, it lists **all** subsets invariant under \(\theta\) and containing both endpoints. These three independently defined sets of equality loci coincide and each has cardinality \(512\); the analogous computation for one FOUR variable gives \(4\). These finite assertions are exhaustive, not samples: the program loops over every Boolean function truth table and every eligible subset. The same enumeration yields the displayed histograms.

**5. Sharp three-variable witness.** Fix \(k=3\), and abbreviate a FOUR valuation by its three entries. Consider the six-element set
\[
S=\{(T,N,N),(B,T,N),(B,B,T),(T,B,B),(N,T,B),(N,N,T)\}.
\]
It is invariant under \(\theta\) and avoids the two extreme valuations. Three of its elements form the strict chain
\[
(T,N,N)<(B,T,N)<(B,B,T).
\]
There is a Boolean-cube point strictly between each adjacent pair **outside** \(S\); explicitly \((B,N,N)\) lies between the first pair and \((B,B,N)\) between the second. Neither belongs to \(S\). Thus a convex subset of \(S\) can contain at most one of these three chain elements. Because \(\theta\) reverses the order, \(\theta(D)\) is convex whenever \(D\) is. No union of two such convex subsets can cover all three chain elements. Hence no eligible \(D\) satisfies \(S=D\cup\theta(D)\), so the invariant endpoint-containing candidate \(E=\mathbf{FOUR}^3\setminus S\) is **not** an equality locus. For \(k>3\), append the \(\theta\)-fixed value \(T\) to the extra coordinates of all six valuations. The same interval obstruction persists, so it fails in every higher arity.

## Verification
Run `python3 verify.py` with standard Python 3. The code directly evaluates the FOUR operations, enumerates all monotone truth-bit functions for one and two variables, exhaustively compares term pairs and invariant endpoint subsets, independently enumerates the convex-disagreement construction, and checks the six-point counterexample. Its success sentinel is `FOUR_EQUALIZER_VERIFY_OK`. The executable computation is necessary for the numerical finite classifications; the all-arity structural theorem and the three-variable obstruction also have the mathematical proofs above.

## Relationship to prior work
Cardó (2026) frames probabilistic spectra of equations in finite algebras but does not classify the equality loci of the Belnap–Dunn FOUR fragment. López (2026) specifies the operations of FOUR in contemporary many-valued logic and studies different truth-functional modal enrichments, not these equation-solution families. Přenosil (2021/2022) studies four-valued equational consequence and logical axiomatizations, not the fixed-arity family of **exact valuation sets** satisfying two formulas. The monotone Boolean representation and order-convex disagreement observation are recognized mathematical ingredients; the sharp two-variable completeness, first three-variable counterexample, and exact pair-count histogram require their specific FOUR coupling through \(\theta\).

## Limitations
The results concern constant-free \(\wedge,\vee,\neg\) only, and do not extend without qualification to expanded four-valued languages or designated-value agreement. The 512-locus statement is specific to two variables. The explicit six-point witness proves failure of the naive invariance criterion for every higher arity but does not enumerate higher-arity loci. Some older clone-theoretic literature is accessible only in abstract; an implicit earlier consequence or alternative formulation cannot be conclusively ruled out. No independent external mathematical audit has been carried out.

## References
1. Carles Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (2026-04-09), https://arxiv.org/html/2604.08446v1.
2. Sandra M. López, *Truth-Functional Modal Expansions for 4-Valued Quasi-Relevant Logics*, *Journal of Logic, Language and Information* (2026-06-19), https://doi.org/10.1007/s10849-026-09482-y.
3. Adam Přenosil, *Four-valued logics of truth, nonfalsity, exact truth, and material equivalence*, arXiv:2111.09978, https://arxiv.org/abs/2111.09978.
4. Alexej P. Pynko, *Functional Completeness and Axiomatizability within Belnap’s Four-Valued Logic and Its Expansions*, *Journal of Applied Non-Classical Logics* 9 (1999), https://doi.org/10.1080/11663081.1999.10510958 (abstract-level comparison; full text not inspected).
