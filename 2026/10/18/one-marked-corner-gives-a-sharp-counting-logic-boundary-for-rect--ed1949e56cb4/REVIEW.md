# Independent mathematical audit

## correctness

PASS

Checked the finite, simple, vertex-coloured 2<=m<=n theorem with exactly one marked corner and arbitrary finite comparison graphs. WL colour classes encode distance from any singleton landmark. For m<n, degree-two corners are distinguishable by distances 0,m-1,n-1,m+n-2 from the marked corner; the corner (m-1,0) is therefore a singleton. The two coordinate distances i+j and m-1-i+j recover each (i,j), forcing a discrete stable partition and C² identification against any graph. For square s, reflection fixes the corner, so classes cannot split coordinate-transpose orbits. Induction on t=i+j uses the multiset of predecessor-orbit colours to separate all unordered coordinate pairs, proving classes precisely X_{i,j}. At s=2,3 all two-element classes are independent and their nontrivial interclass perfect-matchings form a path (none or two links). Every possible classwise pairing is isomorphic via independent flips, and singleton interactions are forced by equitable counts. At all s>=4, switch edges (0,2)-(0,3) and (2,0)-(3,0) to cross edges, preserving equitable neighbours for every orbit and joint 1-WL colours while producing a single 8-cycle instead of two 4-cycles across X02,X03,X13,X12. Those four stable classes are canonically distinguished, so switched graph is nonisomorphic; it remains connected by local detours. Classical C²/1-WL equivalence bridges the claims. Independent separately written exact checker verified 88 grids (77 nonsquares, 11 squares), 9 switched witnesses, 2/3 small-square equitable completions (1 and 4 labelled, each one isomorphism class). Finite runs corroborate, and do not certify the all-size theorem.

## originality

PASS

Best-of-knowledge PASS for the exact uniform side-length boundary, with significant prior structural dependence. Arvind–Köbler–Rattan–Verbitsky (2015, Thm 9) already give an iff characterization of amenable arbitrary graphs, requiring an anisotropic-cell forest; Kiefer–Schweitzer–Selman (2015/2018, Thm 17) give a C² identification iff flip is a bouquet forest. These are genuinely broader and apply to every marked grid. They do not in inspected primary text identify the exact stable partition of the corner-coloured P_m square P_n or state/compute the all-size boundary m<n or m=n<=3. The record adds the all-parameter landmark-distance/orbit-cell analysis and explicit connected switched witnesses, not the general equivalence or forest criterion. The 2026 amenable-symmetry paper addresses distinguishing/fixing numbers of already amenable graphs rather than this classification. An equivalent specialisation or a very short derivation from the 2015 theorems is the main priority/value risk; absence of a search hit alone does not prove novelty.

## value

PASS

A meaningful structural cut-off in the power of one vertex landmark to make a natural two-parameter graph family definable by C². The exact distinction between all nonsquare rectangles and squares of sides 2/3 versus >=4 is not a mere numerical table: it derives from coordinate recovery by a second degree-two corner and the first cycle of two-vertex equitable-orbit interactions. Explicit connected nonisomorphic switched competitors show the failure, rather than just an algorithm negative response. Though the general amenability framework is known, this exact all-size family-specific boundary is a natural independent invariant relevant to individualisation and colour-refinement graph identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
