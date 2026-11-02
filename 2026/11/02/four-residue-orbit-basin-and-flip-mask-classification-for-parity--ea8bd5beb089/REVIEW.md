# Review of the four-residue Kneser-graph orbit, basin, and flip-mask theorem

## Correctness — PASS

The proof determines the entire update matrix \(A=I+B^{\mathsf T}B+J\) over \(\mathbb F_2\), proves both annihilation relations and the rank of the incidence component, and computes \(A^2\) or \(A^3\) in each residue class. The periodic-state dimension is the rank of \(A\); fixed-point counts use the rank of \(A-I\). Uniform basin sizes follow from equal-size fibers of a linear map that is a permutation on its image. The stronger flip-mask classification follows from the explicitly computed image of \(D=A+I\) on periodic states, and the exact mask multiplicities follow from its fiber dimensions. The projection/involution identities prove the result for every \(n\ge5\), independently of finite tests. Two separately written verifiers reconstruct all relevant matrices for \(5\le n\le17\) and exhaustively test configurations for \(5\le n\le7\). The distinctive assumption is *exclusive-neighbor* XOR; the conclusion does not extend automatically to majority updating.

## Originality — PASS with residual risk

The 1991 van Eijl thesis explicitly supplies Smith normal forms of triangular graph adjacency, a closely related complement, and the 2014 Brouwer–Fiol paper studies Kneser distance graph eigenspace structure. Neither inspected material states the four-class binary update law, complete periodic-state and orbit counts, the exact individual basin sizes, or the cut-type flip-mask spectrum and associated per-mask orbit counts. Searches of research records for equivalent two-set disjointness graphs, XOR parity updates, operator polynomial identities, and binary adjacency ranks found no statement dominating the combination. A classical modular rank identity could allow a knowledgeable reader to obtain subsets of the claims by straightforward algebra; no broad first-ever claim about the rank formulas is made. The even-cut/global-complement flip-mask classification is a stronger spatial dynamical assertion not encoded by mere matrix ranks. Historical sources might contain the same dynamics under another vocabulary.

## Mathematical value — PASS

The two-set Kneser graph is a standard highly symmetric family. Its dynamics has a genuinely nonuniform four-class transition between global reversibility, idempotence, and two distinct one-step rank-deficiency mechanisms. The simultaneous exact classification of periods, their multiplicities, first-entry-time cutoff, *all orbit basin sizes*, and the Hamming flip-mask distribution provides motivated natural dynamical invariants across every graph order. The proof uses an explicit structural decomposition rather than a size-by-size census.

## Evidence and limits

The source-date anchor is the first arXiv submission of Brouwer–Fiol, September 1, 2014. The 1991 modular-rank thesis predates that anchor and was inspected for possible coverage; it is not represented as having a known day of first public circulation. Evidence consists of the written proof, independently reconstructed matrix check, and state-by-state C++ check. The latter is necessarily finite. Unindexed earlier formulations and unnoticed consequences of older modular-rank computations remain risks.

Self-review: passed. Independent audit: not yet performed.
