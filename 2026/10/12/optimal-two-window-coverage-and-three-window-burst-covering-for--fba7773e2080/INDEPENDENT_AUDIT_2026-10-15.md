# Independent mathematical audit

## correctness

PASS

PASS: h(a)=(1,a) across F_(2^m), so all 2^m odd-parity syndromes are single positions; even nonzero two-window syndromes are exactly distinct adjacent XORs. If q-1 distinct nonzero differences covered every nonzero field element, the XOR over the group would be 0. On a linear Hamiltonian ordering telescoping gives a_0+a_last !=0; on the cyclic ordering there are q nonzero differences, so exactly one must repeat and XOR would be nonzero. Therefore <=q-2 adjacent labels and <=2q-1 total. Construct order (0,1,alpha,...,alpha^(q-2)), alpha primitive, alpha+1=alpha^t with 2<=t<=q-2. Internal consecutive powers provide all q-1 nonzero labels except Delta=alpha^(t-1), and both head and closing edges repeat labels already present. The positions alpha^j and alpha^(j+2), j=q-2-t in [0,q-4], lie in a linear 3-window and sum to Delta. Thus all syndromes are covered, including m=2. Independently generated GF(8) under x^3+x+1, obtained exactly 15/16 two-window and 16/16 three-window syndromes in both boundary conventions; the infinite proof is the algebraic argument.

## originality

PASS

PASS (best knowledge): The 2026 Sac Himelfarb--Schwartz original defines the metric, proves the local-check characterization (Theorem 13) and gives one length-eight permutation of radius three (Example 16). Theorem 17 is a generic counting inequality, not a sharp all-m one-hole obstruction plus simultaneous explicit construction. Historical additive-group terraces and R-sequencings address permutations with prescribed consecutive differences, but the reviewed work does not visibly contain the coding-theoretic three-window completion or all-m sharp optimum; historical priority risk remains because an analogous near-terrace construction may be unindexed.

## value

PASS

PASS: Localized access to parity-check columns is the motivating cost in burst-covering codes. Establishing a sharp smallest window size, impossibility at width two, exact single uncovered syndrome and an explicit ordering for an infinite classical code family is a natural and reproducible mathematical classification. The result is not falsely described as decoding or correcting burst errors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
