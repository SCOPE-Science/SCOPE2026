# Independent mathematical audit

## correctness

PASS

For q=p^h>=2 and d=q^2+q+1, Fermat C_q over algebraic closure, the Frobenius factorization shows the Taylor coefficient of degree q on the tangent is sum a_i^(q^2+1) e_i^q. On nonzero-coordinate points its vanishing is equivalent to all norm coordinates a_i^d being proportional over F_q, hence the point is defined over F_(q^3), using d(q-1)=q^3-1. Non-rational points have tangent order exactly q. A rational interior tangent has next nonzero coefficient -A0 A1/A2 at degree q+1. Each of three coordinate lines contributes d points of contact d, while the interior norm equation gives (q-2)d^2. Hasse derivative D^(q) of tangent local section has leading coefficient binom(j,q)=1 mod p for j=q,q+1,d, giving Wronskian weights j-q; global degree consistency checked against (q+1)(2g-2)+3d. Independently enumerated GF(8), q=2, d=7 projective curve points via GF(8) multiplication and computed their tangent coefficients: 21 points, all contact order 7. Inspected actual verify_contacts.py for independent finite-field cases q=2,3,4,5; finite checks do not substitute for algebraic proof.

## originality

PASS

Komeda (2020) treats precisely degree q^2+q+1, and the Fermat special member. Accessible full PDF introductory statements show its Theorem 1 flex count applies to the GENERAL member, whereas the Fermat Theorem 2 identifies dual curve and its singularities; the inspected sections do not give this exact all-point contact trichotomy or ramification multiplicities. Standard Stöhr-Voloch ramification gives a method and degree but not the member-specific support without the Frobenius/norm analysis. Qualified originality attaches to this exact special-member computation.

## value

PASS

Natural nonclassical smooth Fermat family, explicit complete tangent osculation order and scheme-theoretic ramification divisor with two rational point strata. The q=2 boundary and arbitrary characteristic are included; this informs dual geometry and Stöhr-Voloch local parameters, not an artificial finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
