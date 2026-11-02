# Scientific review

## Correctness — PASS

The static satisfaction rule uses the four distinct sites at offsets \(\pm1,\pm2\), with weak threshold two; this requires \(n\ge5\). A singleton color-run can meet the threshold only when its two adjacent runs are themselves singletons, so the entire nonconstant ring alternates. With no singletons, any length-two run has a boundary resident with one matching neighbor, so every run has length at least three. Conversely these two classes are satisfied. Counting the \(k\) type-one and \(k\) type-zero runs by positive compositions with parts at least three gives the factor \(n/k\) after accounting for the \(k\) possible marked type-one run starts. Summing across populations gives the univariate formula. A primitive six-state adjacency matrix has characteristic polynomial \((t^3-t^2-1)(t^3-t^2+1)\), yielding the Perron growth constant.

The package contains a standalone Python checker which independently enumerated all binary words up to length 16 and compared each fixed-composition count and classification, and then tested transfer traces up to length 50. It passed 134,474 assertions. Finite checks supplement, not substitute for, the proof.

## Originality — PASS within inspected literature, provisional

The cited 2004 majority-cellular-automaton article explicitly gives the general sufficient stability of long homogeneous runs. A 2022 structural treatment additionally partitions periodic fixed states into strongly stable configurations and short-run exceptions. Thus the run-length building blocks and the structural direction are prior art. The final claim is the explicit **microcanonical** all-satisfied census \(S_{n,m}\) at every fixed population balance and the exact total-state entropy. The inspected 2004 article (including its fixed-point section), the complete 2012 circular Schelling article, the 2011 full text on segregation dynamics, and the 2022 automaton study do not state this binomial census or its six-state entropy. Their general structural machinery could simplify its derivation but does not itself numerically provide it. Research-index searches for radius-two majority fixed-point composition enumeration and Schelling all-happy counts found no exact matching record.

A general fixed-point transfer-matrix method and a possible unlocated explicit sequence/table remain residual historical-priority risks; this self-review is not an independent priority determination.

## Value — PASS

The number \(m\) of residents of each type is conserved by type-swapping versions of the ring model, so \(S_{n,m}\) describes a natural fixed-population invariant, not an arbitrary slice. It gives the exact proportion of configurations with universal satisfaction conditional on group composition and distinguishes the two integrative checkerboards from minimum-run segregated layouts. The all-population entropy quantifies how sparse all-satisfied layouts are under a uniform random initialization. These questions are distinct from, and not answered by, dynamic run-length estimates or the qualitative existence of long-run fixed points.

## Limitations and closest literature

This is a finite-ring, two-type, no-vacancy, uniform-threshold and static-counting result. It does not count all absorbing states of a particular pair-swap dynamics, prove accessibility from initial states, or treat empirical neighborhoods. Directly compared prior sources: Tosic–Agha (2004), Goles Domic–Goles–Rica (2011), Brandt–Immorlica–Kamath–Kleinberg (2012, arXiv:1203.6346), and Nakar–Ron (2022, arXiv:2205.08972). A general counting method or historical table could subsume the explicit census if later located.

Self-review: passed. Independent audit: not yet performed.
