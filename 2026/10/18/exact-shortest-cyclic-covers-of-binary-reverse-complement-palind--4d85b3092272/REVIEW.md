# Scientific assessment

**Correctness — PASS.** A complete finite-state de Bruijn subset-search is a bijective model of rooted indexed cyclic hosts. The shortest-terminal BFS distance proves the minimum length, and shortest-path integer accumulation counts every optimum. An independent overlap-tour subset dynamic program gives the same minima. The supplied source recompiles, checks a concrete cyclic witness at each order, and prints `VERIFY_OK`. The finite scope is exactly \(m=1,2,3,4\); no claim about an infinite pattern is made.

**Originality — PASS against inspected evidence, with residual risk.** The closest work on RC-complete probe sequences (Orenstein–Shamir, 2013) covers all reverse-complement classes of all DNA \(k\)-mers, not only the compulsory fixed-point subset on one binary cycle. Cazaux–Cánovas–Rivals (2016) permit a collection of cycles and either orientation. Moreno–Matamala (2007) use Eulerian cycles of complete restricted languages. Fici and collaborators (2015) study linear superstrings with reversal options. Ordinary palindromes satisfy a different defining relation from reverse-complement palindromes. Searches located no numerical duplicate; continuous full text of the 2013 publisher paper remained inaccessible, and unindexed coverage is possible. These limits are preserved in the originality record.

**Mathematical value — PASS.** Every RC-fixed factor is unavoidable when a double-stranded design must represent all orientation classes. The exact one-cycle optimum for the fixed-point subset is a natural lower-bound benchmark independent of whole-language and multi-cycle designs. Its rooted optimum multiplicity, especially \(1232\) at the first 16-pattern order, is a nontrivial additional invariant useful for studying non-unique optimal periodic probes.

The exact finite computations are reproducible from `verify.cpp`. Independent scientific validation was not carried out.

Self-review: passed. Independent audit: not yet performed.
