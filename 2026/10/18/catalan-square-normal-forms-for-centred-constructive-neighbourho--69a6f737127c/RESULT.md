# Catalan-square normal forms for centred constructive neighbourhood chains

## Finding

Fix a positive integer \(n\), and let \(C_n=\{0<1<\cdots<n-1\}\). In the constructive neighbourhood semantics for intuitionistic monotone modal logic, consider a neighbourhood assignment \(N\) satisfying, at each world \(i\),
\[
N(i)\ne\varnothing,\qquad (\forall a\in N(i))\ i\in a.
\]
Every neighbourhood is therefore nonempty; no monotonicity of the assignment is assumed. Call these **centred-serial** neighbourhood frames. Truth is evaluated by the persistent constructive \(\Box\)- and \(\Diamond\)-clauses described below.

**Theorem.** For every centred-serial neighbourhood frame on \(C_n\), there are unique weakly nondecreasing sequences of integers \(B=(B_0,\ldots,B_{n-1})\) and \(D=(D_0,\ldots,D_{n-1})\) such that
\[
0\le B_i\le i\le D_i<n\quad(0\le i<n)
\]
and its truth values at **every world, under every upset valuation, for every intuitionistic bimodal formula** agree with those of the singleton-neighbourhood frame
\[
N^*(i)=\big\{\{B_i,B_i+1,\ldots,D_i\}\big\}.
\]
Two centred-serial assignments agree on all these truth values if and only if the corresponding ordered pairs \((B,D)\) are equal. Thus the exact number of observational equivalence classes is
\[
\boxed{\operatorname{Cat}_n^2
=\left(\frac{1}{n+1}\binom{2n}{n}\right)^2.}
\]
The numbers for \(n=1,2,3,4,5\) are respectively \(1,4,25,196,1764\). Every class has a **one-neighbourhood-per-world interval representative**, and the representatives are pairwise distinct already at modal depth one.

Here observational equivalence means equality of forcing at every *labelled world* and every valuation, not equivalence of the complete valid-theory sets alone. The original neighbourhood assignments in the same class may be different.

## Assumptions and scope

A constructive neighbourhood frame consists of \((W,\le,N)\), where \(\le\) is an intuitionistic preorder and \(N(w)\subseteq\mathcal P(W)\). An intuitionistic valuation sends each atom to an upward-closed set. Implication satisfies \(w\Vdash\varphi\to\psi\) if every \(v\ge w\) forcing \(\varphi\) also forces \(\psi\).

The two modal clauses are the following, for all formulas \(\varphi\):
\[
\begin{aligned}
w\Vdash\Box\varphi
&\iff \forall v\ge w\ \exists a\in N(v)\ \forall u\in a\ (u\Vdash\varphi),\\
w\Vdash\Diamond\varphi
&\iff \forall v\ge w\ \forall a\in N(v)\ \exists u\in a\ (u\Vdash\varphi).
\end{aligned}
\]
These are the future-world clauses in Dalmonte and de Groot's constructive neighbourhood semantics [1, Definition 2.3]. All Boolean-free intuitionistic connectives, including implication and bottom, and both modalities are allowed; negation is an abbreviation for implication to bottom. The theorem does not require that the modal operators be dual under classical negation.

The restriction that every neighbourhood at \(i\) contains \(i\), together with nonemptiness of each family \(N(i)\), is assumed **as a raw frame condition**. No claim is made that these syntactic conditions are necessary for validating all modal axiom schemes on general preorders. The requirement of a fixed finite chain is essential for replacing each neighbourhood by its least and greatest points when formulas denote upsets.

For each \(i\), put
\[
b_i=\max_{a\in N(i)}\min a,\qquad
d_i=\min_{a\in N(i)}\max a,
\]
and then define the observable suffix thresholds
\[
B_i=\min_{i\le v<n}b_v,\qquad D_i=\min_{i\le v<n}d_v.
\]
Every maximum/minimum exists because the domain and nonempty neighbourhood families are finite. These expressions are a canonical invariant of the original assignment.

## Proof

**1. All formula extensions are upsets.** This holds for atoms by definition, for intuitionistic propositional connectives by the ordinary clauses, and for each modality because its clause at \(i\) quantifies over every \(v\ge i\). If \(i\le j\), the quantifier domain above \(j\) is contained in that above \(i\). Consequently, induction on formulas shows that their truth sets are precisely among
\[
U_t=\{t,t+1,\ldots,n-1\},\quad 0\le t\le n,
\]
where \(U_n=\varnothing\).

**2. Neighbourhood clauses depend only on suffix thresholds.** Let \(\varphi\) have extension \(U_t\). For a nonempty neighbourhood \(a\), the condition \(a\subseteq U_t\) is equivalent to \(\min a\ge t\). Its intersection with \(U_t\) is nonempty exactly when \(\max a\ge t\). Hence at any world \(i\),
\[
\begin{aligned}
i\Vdash\Box\varphi
&\iff \forall v\ge i\ \exists a\in N(v)\ (\min a\ge t)
\iff t\le \min_{v\ge i}\max_{a\in N(v)}\min a
\iff t\le B_i,\\
i\Vdash\Diamond\varphi
&\iff \forall v\ge i\ \forall a\in N(v)\ (\max a\ge t)
\iff t\le \min_{v\ge i}\min_{a\in N(v)}\max a
\iff t\le D_i.
\end{aligned}
\]
The calculation is valid for \(t=n\) as well: no neighbourhood is empty, so both modalities reject an empty truth set under the centred-serial assumptions.

**3. Threshold constraints.** Every \(a\in N(i)\) contains \(i\). Therefore \(\min a\le i\le\max a\), so \(b_i\le i\le d_i\). Taking suffix minima yields \(B_i\le i\) (the suffix includes \(i\)) and \(D_i\ge i\) (every \(d_v\ge v\ge i\)). Both sequences are weakly nondecreasing: increasing \(i\) removes some candidates from each finite minimum. Their entries lie in \(\{0,\ldots,n-1\}\), and thus \(B_i\le D_i\).

**4. Singleton interval normal form.** Conversely choose any weakly nondecreasing \(B,D\) with \(B_i\le i\le D_i\). Let \(N^*(i)\) contain exactly the interval \([B_i,D_i]\cap C_n\). It is centred-serial because it contains \(i\). Its local minima and maxima are exactly \(B_i\) and \(D_i\), and the suffix minima are the same sequences because the sequences are weakly nondecreasing. Step 2 implies that \(N\) and \(N^*\) induce identical modal operators on every upset. Simultaneous structural induction on formulas, using the identical fixed intuitionistic order and valuation, now proves equality of truth at every world for **arbitrarily nested formulas**, not merely modal depth one.

**5. Exactness of the invariant.** Any pair of distinct admissible threshold sequences differs in some component, say \(B_i\ne B'_i\) or \(D_i\ne D'_i\). Choose a propositional atom \(p\) valued in the principal upset \(U_t\), where \(t\) lies strictly above the smaller threshold and at most the larger. By Step 2, \(\Box p\) at \(i\) distinguishes different \(B_i\), and \(\Diamond p\) at \(i\) distinguishes different \(D_i\). Hence no two distinct pairs can be observationally equivalent. This also proves the uniqueness asserted in the theorem.

**6. Catalan enumeration.** Weakly nondecreasing integer sequences
\[
0\le B_0\le B_1\le\cdots\le B_{n-1},\qquad B_i\le i
\]
are counted by the Catalan number \(\operatorname{Cat}_n\): they are equivalently lattice paths from \((0,0)\) to \((n,n)\) that never cross the diagonal, by recording the positions of the successive north steps; the reflection principle gives \(\binom{2n}{n}-\binom{2n}{n+1}\). Reversing the index and complementing values, \(D_i\mapsto n-1-D_{n-1-i}\), gives a bijection from admissible \(D\)-sequences to admissible \(B\)-sequences. There is **no cross-constraint** between their independent choices beyond \(B_i\le i\le D_i\). Every pair is realized by Step 4. Multiplying proves the Catalan-square count.

## Verification

The accompanying standalone `chain_catalan_verify.py` needs only Python's standard library. Run

```sh
python3 chain_catalan_verify.py
```

It constructs every centred-serial neighbourhood family for each world and every total frame on chains of lengths one, two, and three. For each original frame and every upset, it evaluates both future-world modal clauses literally, with no use of the stated formula. It independently extracts \(B,D\), forms the singleton interval frame, and checks equality of the complete pairs of modal truth tables. The exhaustive raw frame counts are respectively \(1\), \(9\), and \(3375\). Their distinguishable behaviours are respectively \(1\), \(4\), and \(25\).

Separately it enumerates all admissible canonical threshold pairs for lengths one through five and checks that all output signatures are different and that their counts equal \(1,4,25,196,1764\). Successful execution prints `CHAIN_CONSTRUCTIVE_NEIGHBOURHOOD_CATALAN_VERIFY_OK`. The exhaustive finite computations test small carriers only; the theorem for all \(n\) is established by the proof above.

## Relationship to prior work

Dalmonte and de Groot [1] introduce the constructive neighbourhood semantics and establish characterizations and a proof calculus for the intuitionistic monotone modal logic and extensions. Their semantic clauses are used here verbatim; the present claim concerns the **observational quotient of centred-serial neighbourhood families on a chain**, a classification and exact enumeration not stated in the inspected motivating work. De Groot's earlier work [2] discusses alternative intuitionistic neighbourhood semantics and translations but does not state the Catalan-square classification here.

Related published work [3] classifies **accessibility relations** on finite intuitionistic chains satisfying two forward/downward confluence axioms, obtaining a weighted count of binary relations rather than a count of observational equivalence classes of neighbourhood families. Work [4] similarly studies the row and column maxima of birelational accessibility relations for intuitionistic tense logic. The objects, hypotheses, output invariants, and implications are different: neither result supplies the local \(\min a/\max a\) thresholds, their future-world suffix minima, or this singleton-family semantic collapse. They are not invoked in the proof.

The reflection-principle Catalan count and ordinary interpretations of monotone maps on chains are classical. The claimed content is the **combination of constructive neighbourhood semantics, faithful single-interval reduction for both modalities at all formula depths, and exact observational quotient classification**. No historical-priority claim is made for either classical counting ingredient in isolation.

## Limitations

The theorem is restricted to finite *chains* and nonempty neighbourhood families whose every member includes its world. A general partial order may lack least and greatest points of a neighbourhood, so the proof does not extend automatically. Allowing empty neighbourhoods or dropping centredness changes the boundary conditions and may change the classification. It counts interpretations distinguishable under all upset valuations and all modal formulas at labelled worlds; it does not count the raw neighbourhood assignments, frames up to unlabelled isomorphism, logics determined solely by validity, or arbitrary neighbourhood semantics with different modal clauses.

Although targeted published-result and literature comparisons did not identify this exact theorem, older order-theoretic or modal-algebraic representation results might imply it under different terminology. Independent historical-priority assessment remains appropriate. The finite checker corroborates only its indicated cases.

## References

[1] Tiziano Dalmonte and Jim de Groot, “Intuitionistic Monotone Modal Logic: Proof Theory and Semantics,” arXiv:2606.31870v1, first publicly posted 30 June 2026; *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 278–298, DOI:10.4204/EPTCS.447.16. Definition 2.3 gives the constructive clauses.

[2] Jim de Groot, “Intuitionistic monotone modal logic via translation,” arXiv:2507.13746v1, first publicly posted 18 July 2025; *Journal of Logic and Computation* 36 (2026), exag017.

[3] “Endpoint normal form and exact census for finite-chain KI frames,” publicly available research result, 2026, 2026 public scientific record, title as given.

[4] “Maxima normal form and exact census for chain birelational relations,” publicly available research result, 2026, 2026 public scientific record, title as given.
