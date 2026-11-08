# Independent mathematical audit

## correctness

PASS

PASS FOR THE REPAIRED FINAL CLAIM. Original RESULT.md Step 3 has an incorrect sign in its n^-1 residual: it prints +Δ−2k where expansion of (1) actually gives +2k−Δ. The printed expression does not cancel for its advertised A,B; independently at λ=1,c=5/13,ρ=1/5 and k=1, it gives −4/13 instead of zero. The complete new RESULT.md fixes the forcing to +2k−Δ, proves Lh=Δ−2k with A=−1/Δ, B=1−(1+λ)/Δ², and then exact cancellation. Gram orthogonality yields tridiagonal M-matrix with row excess ≥1 and l∞ inverse bound ≤1; remaining residual ρ^k n^-2P2(k)+ρ^k n^-3P3(k) is uniformly O(n^-2). Thus all-k coefficient and uniform |z|≥R>1 exterior expansion follow. Independent rational k=1..6 checks gave zero corrected n^-1 coefficient; independent tridiagonal solves for n=30,150,600 gave n² absolute first-coefficient errors around 0.095. The corrected first-order term is a nonzero rational function and all hypotheses λ>0,0<c<1/2 are retained. Full replacement RESULT.md bytes are staged with verified current blob guard and SHA-256; old proof evidence preserved unchanged in Git.

## originality

PASS

PASS best of knowledge. Majumder–Swaminathan arxiv:2610.31994v1 Theorem 3.2/Cor 3.2 gives an exterior leading function depending only on derivative measure μ2 for λ/n². The audited admissible Haar/first-cosine two-measure family instead yields λ-dependent root ρ/(1+ρ²)=λc/(1+λ), with rigorous 1/n correction. The earlier broad theorem printed conclusion is incompatible in this special case, so does not cover the correct claim. Earlier fixed-penalty two-measure and common-measure problems lack this correction; possible earlier Toeplitz recurrence coverage retained.

## value

PASS

PASS. The exactly soluble one-Fourier-mode model yields a sharp critical-scale asymptotic and uniform all-coefficient remainder, and supplies a concrete admissible counterexample to the published derivative-measure-only limit. Such a boundary correction matters for strong asymptotics of varying Sobolev orthogonality; not just a routine parameter substitution. The one-sign correction repairs a real proof gap without changing the valuable theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
