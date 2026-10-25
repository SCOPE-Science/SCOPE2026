# Scientific review: ternary Hamming translation character

## Correctness — PASS

The assertion concerns a finite, explicitly defined 27-vertex simplicial complex. The verified increasing-index enumeration gives 5,949 nonempty faces. The staged matching has 2,951 pairs, leaving only one 0-cell and 46 critical 3-cells; the complete 27,189-incidence directed Hasse graph is acyclic. Thus the rational homology concentration used in the Lefschetz argument is independently reconstructed, not merely imported from a previously published homotopy result. The signed trace computation accounts for the orientation of each invariant simplex: order-three vertex cycles have positive sign. The orbit-complex face vectors are exactly \((9,18,6)\), \((9,9,3)\), and the empty vector for translation weights 1, 2, and 3, giving traces \(4,-2,1\). Orthogonality with \((1-t)^k(1+2t)^{3-k}\) gives the stated integer Fourier multiplicities. The standalone executable independently checks all 27 translations and all nonzero simplicial boundary ranks. No infinite-parameter claim is made.

## Originality — PASS, subject to stated search limits

The closest same-object published research records [4] and [5] establish the nonequivariant wedge of 46 three-spheres and ordinary persistence; those results are explicitly not reclaimed. Their complete `RESULT.md` mathematical statements and proof passages were inspected, and neither computes an \(A\)-character or quotient invariant. Goyal--Shukla--Singh treat two-factor categorical products, and Antolín Camarena--Carnero Bravo prove the triple product only when one factor is binary and otherwise conjecture a homotopy formula; the relevant primary full-text sections show no equivariant calculation. Adamaszek supplies graph-power Rips framework, not this character. The 2026 hypercube representation theorem is restricted to binary alphabets. The neighborhood complex of the same graph is a distinct simplicial complex. Targeted semantic search and primary-literature searches found no implication forcing the four trace values from published results. The remaining risk is an unindexed equivariant computation or an equivalent calculation under another notation.

## Mathematical value — PASS

The ternary three-cube is the first fully nonbinary symmetric triple-product case for which the ordinary Rips homotopy type was separately established. The new statement distinguishes 19 Fourier characters of multiplicity two from eight full-support characters of multiplicity one, and computes the rank-two third homology of a natural finite symmetry quotient. These invariants cannot be reconstructed from the ordinary dimension 46; their shape comes from a nontrivial geometric distinction among three orbit-clique complexes. It provides a reproducible equivariant benchmark without asserting a general multi-parameter classification or paper-sized consequence.

## Scientific and bibliographic limits

The integral \(\mathbb Z[A]\)-module, the full automorphism character, and larger alphabets/dimensions are not determined. Full relevant texts and indexed results were examined, but unindexed equivalent work cannot be ruled out. The matching and Lefschetz checks are complete for the finite object, not general existence proofs for all Hamming metrics.

Self-review: passed. Independent audit: not yet performed.
