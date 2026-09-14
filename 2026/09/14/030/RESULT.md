# Cartan matrix of the S3-C2 two-orbit EI algebra in characteristic 2

## Context

Let k be algebraically closed of characteristic 2 and C a connected skeletal finite EI-category with objects {x,y}, Aut(x)=S3, Aut(y)=C2, C(x,y)=M a 4-point (C2,S3)-biset with orbits 3+1, C(y,x) empty. Its category algebra A=kC is the triangular matrix algebra [[R,0],[M,S]] with R=kS3, S=kC2, dim A=6+4+2=12. Both corners are non-semisimple, so A has infinite global dimension. The admitted target asked to prove the proposed Cartan matrix [[2,1,0],[1,2,0],[2,2,2]] of determinant 6 or disprove it with a corrected exact matrix from certified projective covers.

## Definitions

Order the three simples as S1 = trivial R-module, S2 = 2-dimensional R-module, S3 = trivial S-module, all inflated to A. Cartan entries use rows = projectives: C(A)_{ij} = multiplicity of Sj in Pi. Write a=(123), b=(12), e0=1+a+a^2 in R, and J=1+c with c the generator of C2.

## Result

Theorem. The proposed matrix of determinant 6 is false. The exact Cartan matrix of A is

C(A) = [[2,0,0],[0,1,0],[2,1,2]], det C(A) = 4, rank C(A) = 3.

## Proof and evidence

The computation is an exact pure-Python certificate over F4=F2[w]/(w^2+w+1), which embeds in k, in output/artifacts/certify_cartan.py with ALL_PASS=True. First, e0 is a central idempotent and e0R has basis {e0,e0b} with radical u=e0+e0b square-zero, a 2-dimensional local block of Cartan [2] with unique simple S1. The explicit 2-dimensional representation rho(a)=diag(w,w^2), rho(b)=off-diagonal swap is simple, kills e0, and spans M2, giving an isomorphism (1+e0)R = M2(k); hence the second block is simple artinian with unique simple S2 and Cartan [1]. Thus C(R)=diag(2,1), already contradicting the proposed top-left [[2,1],[1,2]]. Second, brute force over order-4 subgroups of C2xS3 shows exactly 3, all containing central C2x1 and conjugate under 1xS3, so the 3+1 biset is unique and the left C2-action is trivial via the augmentation S->k. Third, M as right R-module is T+T+W: orbit sum u1, fixed point u2 span two trivial lines and the sum-zero-on-orbit subspace W3 is certified simple, with direct rank 4. Fourth, projectives P1=(e0R,0) of dimension 2 with factors 2xS1 and P2=(e1R,0) of dimension 2 and simple S2 follow. P3={(m,s)} of dimension 6 admits the certified submodule chain 0<U1<U2<Mp<V5<P3 of dimensions 1,2,4,5,6 closed under all seven algebra generators, with successive factors S1,S1,S2,S3,S3. The Cartan rows follow, with projective dimensions 2,2,6 satisfying 2*1+2*2+6*1=12=dim A, while the proposed matrix forces projective dimensions 4,5,8 and total 22, impossible.

## Limitations

The statement fixes the simple ordering above, the 3+1 orbit type, and characteristic 2; F4 arithmetic transfers to any algebraically closed field of characteristic 2. It does not classify other biset orbit types or characteristics.

## Reproducibility

Run `python3 output/artifacts/certify_cartan.py`; it writes cartan_certificate.json and exits 0 with ALL_PASS=True.

## References

Chen-Wang, The finite EI categories of Cartan type, J. Algebra 2019 (arXiv:1811.00294), general Cartan-type EI background only. Li (2011, 2014) and Wang (2016) on hereditary, representation-type, and Gorenstein triangular EI theory. Standard modular facts C(kS3)=diag(2,1), C(kC2)=[2] in characteristic 2.
