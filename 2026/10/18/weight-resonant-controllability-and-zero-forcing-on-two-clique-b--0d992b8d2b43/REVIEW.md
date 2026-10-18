# Scientific review: weighted two-clique bridge controllability

## Correctness — PASS

The result is proved for all clique orders \(p,q\ge3\), internal positive conductances \(a,b\), and positive bridge conductance \(c\). The PBH argument reduces every candidate input set to two twin-space cardinality conditions and an explicit one-dimensional residual mode. At the exact rate collision \(ap=bq\), that residual mode makes the baseline sets uncontrollable; each extra selected vertex eliminates it. The zero-forcing criterion is proved independently by a forced-coloring argument, and the counting polynomial follows. The self-contained checker passed 37704 finite assertions on 36 weighted graphs; these do not substitute for the full proof.

## Originality — PASS, subject to residual risk

The closest published record, *Zero forcing polynomial of bridge barbells* (identifier 5431b532d7f2), already gives the zero-forcing enumerator and is fully credited for that fact. The contribution assessed here is the **weight-dependent complete independent-actuator controllability classification** and the exact correspondence with zero forcing only on the resonance hypersurface. Parlangeli–Notarstefano concern paths and cycles (arXiv:1109.3556) and grids (arXiv:1203.0129). Aguilar–Gharesifard study broader graph controllability classes under binary single-input vectors (DOI 10.1109/TAC.2014.2381435). Hsu's interconnection result (arXiv:1808.03022) requires single-input-controllable cells, and Dai's retrieved material (DOI 10.1049/cth2.12385) concerns other example families. None of the inspected statements implies the present iff condition. Full access to some related material was limited; an equivalent formulation elsewhere remains possible.

## Value — PASS

The two-clique barbell is a basic sparse intercommunity bottleneck with dense internal coupling. The result determines **all** admissible independent vertex-controller placements, not just one certificate or an algorithm for testing them, and gives a sharp, physically meaningful resonance \(ap=bq\) that adds exactly one necessary actuator regardless of \(c>0\). The count of optimal placements and the precise difference from zero forcing provide usable network-design information even though the zero-forcing polynomial itself was previously known.

## Limits

The theorem is for uniform intracommunity conductances and one positive bridge, not arbitrary weighted networks or broadcast actuation. No near-resonance conditioning bound or independent mathematical audit is supplied. The literature comparison is nonexhaustive; especially the entirety of the later critical-set and zero-forcing record texts was not available for examination.

Self-review: passed. Independent audit: not yet performed.
