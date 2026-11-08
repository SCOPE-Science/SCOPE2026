# Independent mathematical audit

## correctness

PASS

For closed-neighborhood Boolean update (up,down)=(1,3), a permutation order induces an acyclic orientation; the Macauley–Mortveit cycle-equivalence theorem and single click-equivalence class on trees allow one canonical order per tree. The leaf-augmentation generator with AHU rooted-center canonical tree codes exhausts every unlabeled tree. The C++ code builds every one-sweep successor for every one of 2^n masks and traverses functional graph cycles without skipping transient components; its class counts agree with known unlabeled-tree numbers. Crucially, an independently implemented exhaustive NetworkX nonisomorphic-tree generator and separate C++ state-sweep analysis reproduced for all n=1..14 all 5,447 isomorphism classes, all 65,293,454 finite states, maxima (1,1,1,1,2,3,6,10,14,22,42,58,86,106), maximizing class counts, and orbit counts. The 14-vertex witness states are also given in the inspected trace and witness replay script. Thus the bounded theorem is exhaustive, not sample extrapolation.

## originality

PASS

Macauley–Mortveit already prove cycle-equivalence under sequential update orders; Kuhlman et al. construct long (1,3) cycles on special trees with 3p-2 vertices, explicitly without minimality. Neither inspected primary source states global least-period maxima over all unlabeled trees up to n=14 or uniquely classifies the 106-orbit maximizer. Qualified best-of-knowledge exact finite classification.

## value

PASS

A comprehensive exact finite cutoff of 14 vertices and minimum tree sizes for periods 10,42,58,86,106 are natural, previously unknown graph dynamics invariants; an independent full exhaustive census provides motivated mathematical results even without an all-n formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
