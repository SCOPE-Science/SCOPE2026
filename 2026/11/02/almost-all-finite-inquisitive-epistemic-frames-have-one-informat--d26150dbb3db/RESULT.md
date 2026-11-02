# Almost all finite inquisitive epistemic frames have one information cell: a sharp first-defect asymptotic

## Finding

Let \(F_n\) be the number of **labelled, valuation-free, one-agent inquisitive epistemic frames** on an \(n\)-element world set, with factivity and both positive and negative introspection. Let \(M(m)\) be the Dedekind number counting all downsets, including the empty downset, of \(\mathcal P([m])\), and put

\[
c_m=\sum_{j=0}^{m}(-1)^j\binom mj M(m-j)\quad(m\ge1).
\]

There is an exact enumeration

\[
F_0=1,\qquad \sum_{n\ge0}F_n\frac{z^n}{n!}
=\exp\!\left(\sum_{m\ge1}c_m\frac{z^m}{m!}\right),
\]

where the formal value \(F_0=1\) is used only for the generating function; the semantics assumes a nonempty world set. The counts for \(n=1,\ldots,6\) are \(1,3,16,175,7815,7833957\).

The stronger, asymptotically sharp statement is

\[
F_n-c_n\sim n c_{n-1},\qquad F_n\sim c_n\sim M(n)\qquad(n\to\infty).
\]

Equivalently, a uniformly chosen labelled \(n\)-world inquisitive epistemic frame has a **single information cell** with probability tending to one. Conditional on having more than one information cell, its partition has exactly two blocks of sizes \(n-1\) and \(1\) with probability tending to one. The number of such two-block frames is exactly \(n c_{n-1}\) for \(n\ge3\). The conditioning is over nonuniversal *epistemic accessibility*, not over the number of maximal issue states.

## Assumptions and scope

Fix \(n\ge1\) and a labelled world set \(W=[n]\). A frame consists of a map \(\Sigma:W\to\mathcal P(\mathcal P(W))\). For each \(w\), the family \(\Sigma(w)\) is nonempty and closed under taking subsets. Write \(\sigma(w)=\bigcup\Sigma(w)\). The frame has: (F) factivity \(w\in\sigma(w)\); (PI) positive introspection \(v\in\sigma(w)\Rightarrow\Sigma(v)\subseteq\Sigma(w)\); and (NI) negative introspection \(v\in\sigma(w)\Rightarrow\Sigma(w)\subseteq\Sigma(v)\). Thus PI and NI together assert \(\Sigma(v)=\Sigma(w)\) along the epistemic accessibility relation. Valuations, modal formulas and isomorphism-quotienting are **not** included in \(F_n\). Each labelled assignment of issue families is counted separately.

The component enumeration \(c_m\) is a classical sequence: it counts antichain covers, equivalently abstract simplicial complexes on the full prescribed vertex set (OEIS A006126). Neither that sequence nor the older partition/issue decomposition of inquisitive epistemic frames is claimed new here.

## Proof

**1. Information-cell decomposition.** If \(v\in\sigma(w)\), both introspection axioms imply \(\Sigma(v)=\Sigma(w)\), and hence \(\sigma(v)=\sigma(w)\). Factivity gives \(w\in\sigma(w)\). Therefore the sets \(\sigma(w)\) form an equivalence partition \(\pi\) of \(W\): each set contains its defining world, and two such sets are equal if they intersect. Each block \(B\in\pi\) carries one common downset \(D_B\subseteq\mathcal P(B)\) with \(\bigcup D_B=B\). Conversely, any partition with an independently chosen full-support nonempty downset on each block defines a frame satisfying F, PI and NI. These constructions are mutually inverse. The qualitative decomposition is standard in inquisitive epistemic semantics.

**2. Exact block weights.** For a fixed \(m\)-element block, downsets with union missing a particular designated set \(J\) of \(j\) vertices are precisely downsets of \(\mathcal P([m]\setminus J)\), numbering \(M(m-j)\). Inclusion-exclusion over the missing vertices gives the displayed formula for \(c_m\). In particular \(c_1=1\). Summing the product \(\prod_{B\in\pi}c_{|B|}\) over partitions \(\pi\) proves the exponential generating function by the labelled exponential formula. A completely explicit recurrence is

\[
F_n=\sum_{m=1}^{n}\binom{n-1}{m-1}c_m F_{n-m}\quad(n\ge1).
\]

The first six block weights are \(c_1,\ldots,c_6=1,2,9,114,6894,7785062\), producing the six claimed frame totals.

**3. Dedekind bounds.** Put \(b_m=\binom{m}{\lfloor m/2\rfloor}\). The classical Dedekind estimate, due in its upper-bound form to Kleitman and Markowsky, is

\[
2^{b_m}\le M(m)\le 2^{(1+o(1))b_m}.
\]

A chosen subfamily of the middle layer of \(\mathcal P([m])\) generates a distinct downset. For \(m\ge2\), at most \(2^{b_{m-1}}\) middle-layer subfamilies omit any specified vertex, whence

\[
c_m\ge 2^{b_m}-m2^{b_{m-1}}=2^{b_m}(1-o(1)).
\]

In particular \(c_m\) is exponentially larger, on the \(b_m\)-scale, than \(M(m-1)\). Since every downset that fails to cover all vertices omits at least one of them,

\[
0\le M(m)-c_m\le mM(m-1)=o(M(m)).
\]

Therefore \(c_m/M(m)\to1\). The asymptotics \(b_{m-1}/b_m\to\tfrac12\) and \(b_m\gg m\log m\) will also be used below.

**4. The first nonuniversal partition.** The one-block partition contributes exactly \(c_n\) to \(F_n\). For \(n\ge3\), partitions with two blocks of sizes \(n-1\) and \(1\) contribute exactly \(n c_{n-1}c_1=n c_{n-1}\). Every other partition has at least two blocks, with sizes other than \((n-1,1)\). The sequence \(b_m\) is discretely convex for \(m\ge1\): for every integer \(r\ge1\), the identities \(b_{2r-1}=b_{2r}/2\), \(b_{2r+1}=(2r+1)b_{2r}/(r+1)\), and \(b_{2r+2}=2b_{2r+1}\) show that successive differences are nondecreasing. Moving one vertex from a smaller block of size at least two to a larger block therefore cannot decrease the sum of the \(b\)-values. Iterating, and excluding the unique two-block size shape \((n-1,1)\), leaves at most the shapes \((n-2,2)\) or \((n-2,1,1)\) as maximizers. Since \(b_1=1\) and \(b_2=2\), every such other partition (for \(n\ge4\)) satisfies

\[
\sum_{B\in\pi}b_{|B|}\le b_{n-2}+2.
\]

Fix \(0<\varepsilon<1\). The Kleitman–Markowsky estimate, with finitely many small sizes absorbed into a linear term, supplies a constant \(C_\varepsilon\) such that

\[
\log_2 M(m)\le(1+\varepsilon)b_m+C_\varepsilon m\quad(m\ge1).
\]

There are at most \(n^n\) set partitions. Their total contribution, excluding the one-block and \((n-1,1)\) cases, is at most

\[
n^n 2^{(1+\varepsilon)(b_{n-2}+2)+C_\varepsilon n}
=o(n c_{n-1}),
\]

because \(b_{n-2}/b_{n-1}\to\tfrac12\), \((1+\varepsilon)/2<1\), and \(c_{n-1}\ge2^{b_{n-1}}(1-o(1))\). Hence

\[
F_n=c_n+n c_{n-1}+o(n c_{n-1}).
\]

Finally \(n c_{n-1}/c_n\to0\) by the same bounds, giving \(F_n\sim c_n\sim M(n)\). The conditional probability statement follows by dividing the \((n-1,1)\) contribution by \(F_n-c_n\). No finite enumeration is used to prove the limiting statements.

## Verification

The included standalone `checker.py` generates all downsets of Boolean lattices through four vertices, computes \(M(5)=7581\) independently via the two-slice decomposition, checks the inclusion-exclusion values of \(c_m\), and reproduces the labelled recurrence through five worlds. As a separate semantic cross-check, it directly enumerates all factive introspective issue-family maps on world sets of sizes one, two and three, without using the block-partition formula, and obtains exactly \(1,3,16\). Executing the included file with `python3 checker.py` prints `ALL_CHECKS_OK`. The value at six worlds is obtained by applying the recurrence to the independently published Dedekind value \(M(6)=7828354\); the checker does not exhaustively enumerate six-world frames.

## Relationship to prior work

Müller (2026) supplies the current geometric frame-language treatment and explicitly lists factivity, positive introspection and negative introspection. Ciardelli and Otto (2024) already formalize the S5-like inquisitive epistemic semantics and the partition/constant-issue decomposition; those are not new contributions of this result. The numerical weights \(c_m\) are the known antichain-cover / all-vertices simplicial-complex numbers (OEIS A006126). The labelled exponential formula is the standard combinatorial composition operation. Kleitman and Markowsky (1975) provide the established growth estimate for Dedekind numbers.

The result assessed here is specifically the **sharp first-defect concentration law for the full class of labelled epistemic inquisitive frames**, together with its explicit whole-frame counting formula. The inspected source texts and research records did not supply that probabilistic statement or a stronger theorem specializing to it; this is a bounded literature comparison, not an absolute claim of historical uniqueness.

## Limitations

The asymptotic is for **uniform labelled frames**, without propositional valuations and for one agent. It is not a statement about uniformly sampled epistemic structures up to isomorphism, model-theoretic equivalence, or typical modal validity. Allowing finitely many independently named agents changes the sampling distribution; the one-agent concentration statement is not automatically claimed for arbitrary joint structural constraints. The theorem relies on the classical Dedekind upper bound. Independent mathematical review and historical-priority verification beyond the inspected sources have not been performed.

## References

1. Valentin Müller, *Geometric theories in inquisitive modal logic*, Journal of Logic and Computation 36 (2026), exaf082, first published 2026-03-30, https://doi.org/10.1093/logcom/exaf082.
2. Ivano Ciardelli and Martin Otto, *On the expressive power of inquisitive epistemic logic*, Journal of Symbolic Logic (online 2024), https://doi.org/10.1017/jsl.2024.86. Lawful author manuscript: https://www2.mathematik.tu-darmstadt.de/~otto/papers/InqS5finalNov24.pdf.
3. Daniel J. Kleitman and George Markowsky, *On Dedekind's problem: The number of isotone Boolean functions. II*, Transactions of the AMS 213 (1975), 373–390, https://doi.org/10.2307/1998052.
4. OEIS A006126, *Number of antichain covers of a labeled n-set*, https://oeis.org/A006126 (existing block-weight enumeration, not asserted new).
