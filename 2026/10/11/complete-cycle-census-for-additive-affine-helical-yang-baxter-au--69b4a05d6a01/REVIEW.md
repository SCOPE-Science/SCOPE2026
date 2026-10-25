# Scientific review

## Claim assessed

For every \(m,N\ge1\), all invertible additive-affine Yang--Baxter rules \(f(x)=Lx+c\) over \(\mathbb F_2^m\) have \(L^2=I\). Their full helical site-and-carrier map has only primitive periods \(1,2,4\); the number of full fixed states is \(q(q/2^r)^N\) when \(c\in\operatorname{im}(I+L)\) and zero otherwise, with a parity-dependent two-sweep translation and exact square-zero-rank rule census.

## Correctness — PASS

Substitution into the functional equation gives \((L+L^3)x+(I+L^2)c=0\), hence \(L^2=I\) for invertible \(L\). Put \(D=I+L\), \(D^2=0\), \(r=\operatorname{rank}D\), and \(v=Dc\). The carrier increments obey \(\delta_j=Dx_j+Db_0+(j-1)v+c\). In the second sweep, \(\delta_j'=\delta_j+(N+1)v\); the carrier returns, the sites acquire \((N+1)v\), and \(T^4=I\). Fixed full states are exactly independent kernel fibers when \(c\in\operatorname{im}D\). Image/kernel flags give the rankwise matrix count. Independent direct exhaustive finite checks cover all binary affine rules through dimension three, and a complete rank histogram of the 65,536 dimension-four endomorphisms; these checks corroborate but do not replace the general proof.

## Originality — PASS, best of knowledge

Araoka and Tokihiro (arXiv:2602.17148v1, Sections 2.2--3.2) already establish the underlying equation, helical construction, additive involutions and certain small-field qualitative period results. OEIS A053722 already counts linear involutions. Those prior facts are credited. The simultaneous all-dimension, all-length count of primitive *full-state* orbits according to rank, translation and lattice parity is not stated or implied by the inspected primary results or relevant published affine-CA comparisons. The published June 2026 journal abstract has the same qualitative scope. An inaccessible related two-site manuscript and possible unknown equivalent transfer-map formulations remain priority risks. A matching database record is the present result itself, not independent novelty evidence.

## Mathematical value — PASS

This resolves a natural quantitative invariant of the helical automaton on a complete affine subclass: precisely how many period-one, period-two and period-four full orbits occur for every rule and length. The all-four-cycle criterion and rule-family stratification add mathematical information beyond maximal-period observations and tabulated involutions. This does not settle nonlinear Yang--Baxter maps or projected site-only cycle counts.

## Verification boundary

The all-parameter claims follow from algebraic identities and finite-dimensional flag counting. The independent finite enumeration is a diagnostic, not an exhaustive argument for unbounded parameters. No formal proof-assistant or human expert attestation is asserted.

## Primary references

- A. Araoka and T. Tokihiro, *Integrable cellular automata on finite fields of order 2^n*, arXiv:2602.17148v1 (2026), https://arxiv.org/html/2602.17148.
- Same authors, journal version, *Mathematical Physics, Analysis and Geometry* 29, 30 (2026), https://doi.org/10.1007/s11040-026-09569-9.
- OEIS A053722, https://oeis.org/A053722 (classical involution numbers only).
