# Maximum spectral radius for strongly connected digraphs with n+2 arcs

> **Review status: same-model review.** the same-model review reports a proof of both parts of Klech's Conjecture 5.15, but the proof has not received independent review. Originality is claimed only to the best of our knowledge.

## Claim reported by the source report

Let `G` be a finite strongly connected simple digraph with `n>=3` vertices and exactly `n+2` arcs.

### Loops allowed

Let `R_n` be the unique root in `(0,1)` of

`1-r-r^2-r^(n-1)=0`.

Then the source report claims

`rho(G) <= 1/R_n`,

with equality exactly for the directed flower consisting of cycles of lengths `1,2,n-1` sharing one common vertex.

### Loopless

For `n>=4`, let `Rhat_n` be the unique root in `(0,1)` of

`1-2r^2-r^(n-2)=0`.

Then

`rho(G) <= 1/Rhat_n`,

with equality exactly for the directed rose consisting of cycles of lengths `2,2,n-2` sharing one common vertex.

For loopless `n=3`, the source report states that the unique isomorphism class is the bidirected triangle with one arc deleted and spectral radius `(1+sqrt(5))/2`.

These statements are the exact maximum claims posed as Conjecture 5.15 in Rostislav Klech's September 2026 preprint arXiv:2609.18367v1.

## Branch compression

Strong connectivity gives `d^+(v)>=1` for every vertex, while the arc count gives

`sum_v (d^+(v)-1)=2`.

Hence only two branching patterns are possible:

1. one vertex has outdegree three; or
2. two vertices have outdegree two;

all other vertices have outdegree one.

Put `lambda=rho(G)` and `r=1/lambda`. Eliminating deterministic outdegree-one chains from a positive Perron eigenvector turns a first-hit route of length `L` between branch vertices into the monomial `r^L`.

## One branch vertex

The three return-route lengths `l_1,l_2,l_3` satisfy

`l_1+l_2+l_3 >= n+2`

and

`1=r^l_1+r^l_2+r^l_3`.

With loops, at most one route can have length one. The source report uses convexity to bound the sum by

`r+r^2+r^(n-1)`.

Without loops all three lengths are at least two, giving

`2r^2+r^(n-2)`.

Equality forces the candidate petal lengths and equality in the vertex-cover count, yielding the stated extremal flower/rose.

## Two branch vertices

Compressing the four first-hit routes gives a `2 x 2` nonnegative irreducible matrix `M(r)`. At the actual reciprocal Perron root, `rho(M(r))=1`, while every entry is strictly increasing in `r`.

The source report divides the destination pattern into three forms.

### A. One mixed branch, one cross-only branch

`M=[[r^a,r^b],[r^c+r^d,0]]`.

The condition `rho(M)<1` becomes

`r^a+r^(b+c)+r^(b+d)<1`.

Route coverage and simplicity, followed by convex spreading, reduce this to a strict bound by the candidate one-branch polynomial.

### B. Both branches mixed

`M=[[r^a,r^b],[r^c,r^d]]`.

Here

`rho(M)<1`

is equivalent to

`(1-r^a)(1-r^d)>r^(b+c)`.

The source report uses concavity of `log(1-r^x)` at fixed `a+d`, reduces the remaining one-variable inequality to endpoint cases, and verifies those endpoints at the candidate roots.

### C. Both branches cross-only

`M=[[0,r^a+r^b],[r^c+r^d,0]]`.

A pair of parallel macro-routes cannot both have length one. Convexity bounds each pair by its most spread feasible lengths, after which the candidate-root identities make the product strictly below one.

Thus every two-branch topology is strictly subextremal in the source proof.

## Computational corroboration

The source report states exhaustive labelled enumeration of every simple strongly connected digraph with `n+2` arcs for `n=3,4,5`, both with loops and without loops. The observed maxima agree with the claimed formulas to below `9e-16`.

This computation is corroboration only. The source report's executable checker and captured output are archived as `artifacts/verify.py` and `artifacts/verification_output.txt`.

## Closest prior work

- Klech, arXiv:2609.18367v1, explicitly formulates the exact global maximum problem as Conjecture 5.15.
- Shan, Wang and He, arXiv:2105.03077 / LMA 70 (2022), treat extremal results inside rose, generalized-theta and tri-ring subclasses.
- The source report also identifies Guo--Liu (LAA 437, 2012), Lin--Shu (LAA 436, 2012), and Jin--Zhang (arXiv:1509.07372) as nearby work.

The claimed new content is the global elimination of the two-branch topologies, not the within-rose comparison already present in earlier literature.

## Limitations

The full Guo--Liu 2012 text was not inspected in the source report. The parent preprint was only one day old, so unindexed contemporaneous work is a material originality risk. The proof remains a same-model review rather than independent validation.
