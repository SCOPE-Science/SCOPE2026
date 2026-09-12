# Parity Separation Theorem for the Binomial Family
# f_n = a^n b a^n - b^{n+1} in Q<a,b>

## 1. The separating representation (exact integers, hence valid over Q)

Let A = (a_{ij}), B = (b_{ij}) in M_4(Z) be

A = shift-by-one 4-cycle:  A[i][(i+1) mod 4] = 1, else 0, i.e.
    A = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]];
B = diag(1,0,1,0).

Define rho: Q<a,b> -> M_4(Q) by rho(a) = A, rho(b) = B.
This is a unital Q-algebra homomorphism by the universal property of the free algebra.

## 2. Statement

For every integer n >= 0:  rho(f_n) = 0  iff  n is even.
In particular rho(f_2) = 0 and rho(f_3) != 0.

## 3. Proof

B is an idempotent diagonal projector: B^2 = B (check: diag entries satisfy 1^2=1, 0^2=0).
Hence for every k >= 1, B^k = B.

Conjugation by the cycle permutes diagonal entries: for any diagonal D = diag(d_0,...,d_3),
A D A^{-1} = diag(d_3, d_0, d_1, d_2) (backward rotation). Directly from
A^n = sum_i E_{i,i+n} and B = sum_k b_k E_{k,k} with b = (1,0,1,0), matrix
multiplication gives the exact sandwich formula

  A^n B A^n = sum_i b_{i+n} E_{i,i+2n}   (indices mod 4).

Hence the diagonal entry (A^n B A^n)[i][i] equals b_{i+n} when 2n == 0 mod 4
and 0 otherwise. A short case check on n mod 4 gives:

- n even: 2n == 0 mod 4, so A^n B A^n = diag(b_{i+n}) = diag(b_i) = B, using
  2-periodicity b_{i+n} = b_i for n even. Since B^2 = B, B^{n+1} = B, so
  rho(f_n) = B - B = 0.
- n odd: 2n == 2 mod 4 != 0, so A^n B A^n has zero diagonal (it is purely
  off-diagonal, supported on positions (i, i+2n) with i+2n != i mod 4).
  Therefore f_n = (off-diagonal matrix) - B has diagonal
  (0,0,0,0) - (1,0,1,0) = (-1,0,-1,0), hence is explicitly nonzero.

Therefore rho(f_2) = 0 (zero matrix) while
rho(f_3) = [[-1,0,0,0],[0,0,0,1],[0,0,-1,0],[0,1,0,0]] != 0
(directly: A^3 B A^3 = [[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,1,0,0]], zero diagonal
with off-diagonal spikes; minus B^4 = B gives the matrix above, whose
diagonal (-1,0,-1,0) already witnesses nonvanishing).

Machine check: output/artifacts/verify_parity.py verifies f_n == 0 iff n even for
n = 2..12 over Z (exact integer arithmetic), confirming the hand proof.

## 4. Consequence (what it establishes toward the target)

Let pi: Q<a,b> -> Q<a,b>/(f_2) be the quotient map. Since rho(f_2) = 0, rho factors
uniquely as rho = sigma . pi with sigma: Q<a,b>/(f_2) -> M_4(Q) a unital
Q-algebra map. Since sigma(pi(f_3)) = rho(f_3) != 0, pi(f_3) != 0, i.e.
f_3 is NOT in the two-sided ideal (f_2). Hence (f_2) != (f_2, f_3, ...):
a single generator f_2 does not suffice; the chain of ideals
(f_2) ⊂ (f_2, f_3) is strict. This is the M = 2 base case of the target's
non-finite-generation direction, proved completely and rigorously.

## 5. Classification lemma (monomial/cycle-plus-projector representations)

Within the class A = L-cycle shift, B = diagonal 0-1 projector diag(1_S):
f_n maps to 0 iff (2n ≡ 0 mod L and S + n = S as subsets of Z/L), with the
degenerate case S = empty giving the zero representation (all f_n vanish).
Proof: A^n B A^{-n} rotates the support S by n; B^{n+1} = B for S nonempty
(idempotent) and 0 for S empty; A^n B A^n = rotation by n composed with A^{2n},
and the condition 2n ≡ 0 mod L plus S-invariance is exactly rotation-invariance.
Verified exhaustively for L <= 8, n = 2..10 in output/artifacts/verify_monomial.py.
Corollary: no representation in this class kills f_2, f_3 while keeping some later
f_N nonzero -- even-index zero-sets always come in full even families
(e.g. {2,4,6,8,10}), delimiting this ansatz and motivating the non-monomial search.
