# Independent mathematical audit

## correctness

PASS

For C3 over C, z=2e1, u=e2+i e3, v=e2-i e3 satisfy uv=z and every other basis product zero. Writing a general operator and independently evaluating nine Nijenhuis basis-pair torsions forces N(z)=az and K^TJK=0 for J=[[0,1],[1,0]], with unrestricted covector ell. The algebra automorphism group has connected component [[pq,rho,sigma],[0,p,0],[0,0,q]] and the component swapping u,v, so K transforms by conjugation and ell by (pq ell+rK)diag(p,q)^-1. Any nonzero K has image an isotropic line; after swapping, K=[[t,s],[0,0]], split s=0,t!=0 versus s!=0. In the first case the residual covector quotient has a zero/nonzero flag; in the second, normalize s to 1 and the same flag. With K=0, ell has three orbits: zero, isotropic support, nonisotropic support. This gives exactly 3 Z families, 2 P families (t nonzero), 2 R families (t arbitrary), with a and t invariants. An independent SymPy calculation reproduced the torsion generators; independent full C3(F3) enumeration found 459 Nijenhuis operators, 72 automorphisms and exactly 39 orbits, matching the predicted list. F3 corroborates only; the complex proof supplies universality.

## originality

PASS

Gao–Kang–Lü–Yu / Zou–Gao–Kang–Lü explicitly list raw parametric Nijenhuis operators for the same algebra C3, but the full primary text says an automorphism-conjugacy classification is outside its scope and only illustrates a distinct A5 two-dimensional case. The seven orbit families are not synonyms for the five raw coordinate families: they quotient the full automorphism group using the form K^TJK and eliminate redundancies, retaining trace, kernel type and covector flags. Resultary searches for exact C3 isotropic conjugacy found only unrelated algebras and operator structures; this is supporting scope comparison, not proof that every unindexed treatment has been excluded.

## value

PASS

The published authors identify automorphism-orbit reduction as missing after listing all Nijenhuis operators. Completing the intrinsic seven-family orbit classification for this natural 3D algebra answers that explicit structural problem and makes stabilizers/degeneration parameters transparent; this is not cosmetic relabeling of a raw list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
