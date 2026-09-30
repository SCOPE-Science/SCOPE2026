# Independent audit — 2026-09-29

Record: `2026/09/18/pairwise-incidence-rigidity-transitive-hypersurfaces--ee843b01afbe`  
Assigned and audited source tree: `0784bac7ac2b0e5ae15384310f23e66ba4fd6064`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The globalization argument is sound. Transitivity makes the member tangent to a prescribed hyperplane at a prescribed point unique, so distinct members cannot be tangent where they meet. This gives linear independence of the two x-covectors in the pair-incidence equations and hence a submersion to the ordered configuration space. Martins’ classification makes the ambient manifold compact; properness plus the connectedness of the ordered two-point configuration space makes the nonempty open-and-closed incidence image all of F_2(P), and Ehresmann then gives a fiber bundle. A nearby member is a normal section over a fixed member; Martins’ regular-zero-set theorem identifies the infinitesimal zero set with an equator or projective hyperplane, and stability plus bundle connectivity propagates the fiber type. Fixing one member and pulling the proper submersion back along paths gives the claimed ambient-isotopy class. The argument also handles the one-sided normal line bundle case because only normal sections and their zero sets are used.

## Originality

**supported_qualified_current**. The current Martins preprint supplies the transitive-family classification and the infinitesimal nodal model, but the inspected current text does not state an arbitrary-pair incidence bundle or the conclusion that every distinct pair has the standard codimension-two intersection and isotopy class. Searches of the cited Zoll-family literature did not locate that globalization. The claim is therefore supported narrowly as the arbitrary-pair globalization; the parent paper is extremely recent, so concurrent or unindexed work remains a material but non-decisive risk.

## Scientific value

**meaningful_globalization**. The theorem turns local projective incidence information into a global two-member rigidity statement that survives in transitive sphere families not globally conjugate to the round model. The configuration-space bundle and the dimension-three single-circle consequence are reusable structural information, while the record correctly avoids claims about triple intersections or simultaneous straightening.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/pairwise-incidence-rigidity-transitive-hypersurfaces--ee843b01afbe
- https://arxiv.org/abs/2609.20689
- https://arxiv.org/abs/2112.01448
- https://arxiv.org/abs/2501.16032
- https://doi.org/10.4310/jdg/1090351530

## Limitations

- The result controls pairwise incidence only; it does not constrain triple or higher intersections.
- The sphere-family classification in Martins is topological at the parameter-space level, but path connectedness is all the bundle argument needs.
- Originality is qualified because the principal source appeared in September 2026 and a contemporaneous formulation may not yet be indexed.
