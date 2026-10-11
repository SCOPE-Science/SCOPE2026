---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem concerns \(G_p=\mathbb F_p^3\), \(A_p=\{0,e_1,e_2,e_3\}\), and **distinct** character frequencies \(B\). Let \(\omega=\exp(2\pi i/p)\) and \(M_{a,b}=\omega^{a\cdot b}\). Direct multiplication shows that every diagonal entry of \(M_BM_B^*\) is \(|B|\), and each off-diagonal entry is a root sum associated with one of
\[
D_p=\{e_1,e_2,e_3,e_1-e_2,e_1-e_3,e_2-e_3\}.
\]
The cyclotomic identity \(\Phi_p(z)=1+z+\cdots+z^{p-1}\) makes the vanishing of each such sum exactly equivalent to uniform residue counts. Therefore tightness requires \(p\mid|B|\) and \(|B|\ge4\), by rank. This is a mathematical proof for **every prime**.

At \(p=2\), the two even/odd parity planes both satisfy the six balanced-difference conditions. Fourier inversion forces their uniqueness. At \(p\ge5\), the line \(\{t(1,2,3):t\in\mathbb F_p\}\) has uniform image under all six linear forms because their values on \((1,2,3)\) are nonzero mod \(p\). These prove the exact endpoints without computer enumeration.

At \(p=3\), the representative set \(B_0=\{000,011,102,120,212,221\}\) has residue histograms \((2,2,2)\) for each of the six difference directions. Every six-frequency optimum containing zero belongs to the following **complete list**, presented as sorted triples:

```text
000 011 102 120 212 221
000 012 101 122 210 221
000 012 102 121 211 220
000 021 110 122 201 212
000 021 112 120 202 211
000 022 112 121 201 210
```

Every row equals \(B_0-b\) for one of the six elements \(b\in B_0\). Every unnormalized optimum can be translated through zero and hence belongs to the orbit of \(B_0\). No nonzero period fixes \(B_0\), because it contains no three-point affine line. Therefore exactly \(27\) labelled frequency sets minimize the frame size.

## Standalone replay
Run the included complete source code:

```text
python3 verify_tetrahedron.py
```

The script uses only the Python standard library and exact integer arithmetic. It enumerates all \(\binom{8}{4}=70\) binary candidates and all \(\binom{27}{6}=296{,}010\) ternary candidates; a second normalized enumeration independently checks all \(\binom{26}{5}=65{,}780\) six-sets containing zero. It tests each of the six difference-direction residue histograms, checks all four-by-four ternary Gram entries in the integer basis of \(\mathbb Z[\omega]\), and compares the optimizer set to the explicit translation orbit.

The verified output is:

```text
p=2: tested 70 four-frequency sets; optimizers: 2
p=3: tested 296010 six-frequency sets; optimizers: 27
p=3 normalized: tested 65780 six-frequency sets through zero; optimizers: 6
p>=5: integer witness checks p=5,7,11,13 passed; general proof is symbolic.
```

These finite loops **do not** purport to prove the claim for all primes. The all-prime case follows from the cyclotomic argument and symbolic line construction. The counting invariant is about distinct subsets of the group dual, not weights, multisets, unitary-equivalence classes, or a classification for higher-dimensional simplices.
