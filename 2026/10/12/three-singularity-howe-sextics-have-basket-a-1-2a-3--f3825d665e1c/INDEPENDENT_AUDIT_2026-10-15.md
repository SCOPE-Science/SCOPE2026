# Independent mathematical audit

## correctness

PASS

For absolutely irreducible degree-six Moriya-Kudo (2,2,4) Howe model (char 0 or >=7), arithmetic genus (6-1)(6-2)/2=10; smooth Howe normalization genus 5 forces total delta 5. Primary Prop 4.2.6 proves exactly 3 singular points in Cases II/III, the distinguished (0:0:1) is an ordinary node delta1; two others exchanged by involution have equal delta=2. In Case III the source Lemma 4.2.4 proves nonzero quadratic U² with remaining transverse order >=4. Involution v->-v and uniqueness of splitting critical section make h(v) even; delta(U²-h(v))=floor(ord h/2) gives ord h=4 and A3. In Case II triple-root coefficient alternative (Lemma 4.2.2 system2) eliminates pure u² at infinity. Since multiplicity exactly 2 the tangent quadratic is pure v² and remaining transverse u order 3; local cusp A2 has delta1, contradicting the forced delta2, thus impossible. Remaining double-root case has nonzero u²; a nonzero v² would make node delta1; symmetry again forces transverse order 4 and A3. Independent genus/delta arithmetic checked; source verify.py computes an exact example over F31, which is not proof for all characteristics. No claim for generic 5-point case or char 2,3,5.

## originality

PASS

Moriya-Kudo Proposition 4.2.6 gives three-or-five multiplicity-two points and Lemma4.2.4 type A_{α-1} with α>=4, not alpha=4. Their Lemma4.2.2 preserves a second coefficient system, whereas combining genus defect, paired symmetry and formal parity rules it out. The 2024 companion treats the different (1,1,0) Howe parameter type, and does not subsume the exact (2,2,4) analytic basket. Exact ADE types are a meaningful extra singularity classification although proof uses established genus and splitting tools.

## value

PASS

Analytic singularity basket is a natural geometric invariant of an explicit genus-five plane model, sharper than number/multiplicity of points: A1+2A3 determines local delta distribution and deformation/resolution structure, and removing a spurious parameter alternative clarifies the model family. It is bounded but independently useful geometry rather than a new name for old multiplicity count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
