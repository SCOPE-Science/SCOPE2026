# Independent mathematical audit

## correctness

PASS

For each base q>=2 and each nonempty length-k pattern, explicit failure-function prefix DFAO has qk active (prefix,residue) states and one extra leading-zero initial state exactly when pattern starts with zero. Reachability follows separated one-match words; equal-residue states with different prefix memory are separated by a completion suffix; singleton-zero initial state is distinguished at the unpadded expansion n=0. This establishes minimality even composite q. In binary for k>=2 every state has a unique incoming input label, so no inhomogeneous path, opacity0; for q>=3 distinct nonpattern digits cause shortest inhomogeneous path length2, opacity1; binary singleton zero has length3, opacity1/2, singleton one length2, opacity1. The cited general Allouche--Yao shortest-heterogeneous-path criterion gives the exact normalizations. Inspected bundled verifier; its 1368 pattern/846900 direct-value checks corroborate only finite cases, not infinite proof.

## originality

PASS

Allouche--Yao (2024) define the opacity metric and its general shortest-inhomogeneous-path graph characterization, and compute isolated classical binary automatic sequences, while Abram--Hu--Li (2023) define block-counting family and provide a prefix-state distinguishability argument. Combining them yields a parameter-uniform q,k,pattern opacity phase transition and exact DFAO size not given in the inspected relevant results. Previously known singleton binary examples are not reclaimed.

## value

PASS

A complete binary-versus-higher-alphabet transparency classification for a natural family of overlapping pattern-count automatic sequences identifies a sharp and surprising alphabet threshold, with an exact state-complexity invariant and careful zero-leading boundary cases; this is a motivated infinite-family classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
