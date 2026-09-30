# Same-model scientific review

## Correctness assessment
**PASS.** For a fixed assignment of tuple positions to the two named sides, homogeneity reduces the orbit problem to the action on a binary cross-type matrix. The global complement, left-switch, right-switch, and two-sided switch groups act by translation subspaces of dimensions \(1\), \(a\), \(b\), and \(a+b-1\), respectively. The quotient dimensions therefore give exactly the claimed powers of two. Summation over the \(\binom{k}{a}\) side assignments gives the injective formulas, and equality partitions give the Stirling transform for arbitrary tuples. Edge cases \(k=0,1,2\) were checked explicitly. `verify.py` exhaustively enumerates representative finite matrix actions and independently recomputes the initial profiles.

## Originality assessment
**PASS, best of knowledge.** The closest primary source is Lu's reduct classification, which defines the switch groups and gives finite parity characterizations, but does not state the closed orbit-count formulas, Stirling transforms, growth laws, or the all-arity equality of the \(S_l(\Gamma)\) and \(S_r(\Gamma)\) profiles. Targeted semantic searches for the source, formulas, initial sequences, and profile collision found no equivalent published-finding corpus record or stronger published claim. Recent general oligomorphic-group work provides context but not these exact profiles.

## Value assessment
**PASS.** The formulas compress the finite restrictions of five closed permutation groups into explicit profile sequences and asymptotic growth classes. The equality
\[
f_{S_l(\Gamma)}(k)=f_{S_r(\Gamma)}(k)
\]
for every \(k\), despite the groups being distinct in the reduct lattice, is a substantive structural consequence: the complete ordered-tuple orbit profile does not determine the closed group in this example.

## Closest literature
- Yun Lu, “Reducts of the random bipartite graph,” arXiv:1101.1947; DOI 10.1215/00294527-1731371. This supplies the group classification, switch definitions, and parity invariants.
- Nate Harman and Andrew Snowden, “Oligomorphic groups and tensor categories,” DOI 10.1007/s00222-026-01452-2. This supplies current general oligomorphic-group context and treats bipartite graphs as standard homogeneous examples.

## Scientific limitations
The originality check is targeted rather than logically exhaustive. The result is only for the named-side, side-preserving reduct groups in Lu's theorem. Small-instance computation supports the formulas but does not constitute an independent proof or external validation.

Same-model review: passed. Independent audit: not yet performed.
