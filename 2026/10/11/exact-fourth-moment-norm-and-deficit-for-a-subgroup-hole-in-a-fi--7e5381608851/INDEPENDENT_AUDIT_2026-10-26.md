# Independent mathematical audit

## correctness

PASS

Fresh derivation of the repaired exact identity: Fourier averaging over H annihilates all K-perpendicular frequencies, forcing z_C in the complex zero-sum space V_C for each H coset. The projected coordinate vectors p_j have frame operator sum p_j p_j^*=I_V. The Gram matrix of their rank-one projectors E_j has diagonal (m-1)^2/m^2 and off-diagonal 1/m^2; the induced real Hermitian-frame operator has scalar eigenvalue (m-1)/m, traceless-simplex eigenvalue (m-2)/m, and zero on the perpendicular complement. For A=zz*, B=A-SI_V/(m-1), ||B||_HS^2=S^2(m-2)/(m-1), giving sum |z_j|^4=S^2/m+(m-2)/m||Proj_W B||_HS^2. Subtracting this from alpha_m S^2 gives exactly (m-2)/m||R||_HS^2. Summing over cosets expands (sum S_C)^2, producing 2 alpha_m sum_{C<D} S_C S_D and the full normalized N-scale identity. The m=2 case has W=0 and coefficient zero; N=2, k=1 is admissible. Evaluation coefficients c conjugate(chi(y)) yield f=c(N delta_y-k 1_{y+H}), with all mass in one coset and R=0, so the known norm value is indeed sharp. Bounded independent numerical checks: 220 local/global randomly generated complex zero-sum test cases for m=2..12, 1..5 cosets, max normalized error 4.22e-16; not proof of all dimensions.

## originality

PASS

Repaired claim narrows novelty to the full exact two-scale Hilbert--Schmidt defect, not the sharp norm. Zhang (May 2026), Theorem 2 and complex vector extension, already prove the sharp zero-sum ℓ4/ℓ2 constant in every dimension m, and elementary coset decomposition immediately implies the subgroup-hole K4 formula. Holevo--Utkin earlier state the q=4 extremal formula and establish d=3; published Resultary co-singleton result is a covered case. None of the inspected original/source publications states the global split of the entire deficit into cross-coset S_C S_D and local squared frame-projection remainders. This is an exact identity for every f, not derivable as a stated implication of only a bound on the maximum. Qualified best-of-knowledge; the regular-simplex spectral computation is elementary, and an existing general frame/purity formula might imply the local identity.

## value

PASS

The dual subgroup hole and its annihilator cosets form a natural conditional-expectation subspace. While the sharp norm is known, an all-input exact two-scale stability formula quantifies separately global mass splitting and the local rank-one Hermitian departure from the regular-simplex measurement span. It is a substantive structural identity with a nonnegative geometric remainder and an exact equality criterion, not a single numerical table entry, arbitrary slice, or a reinterpretation of the norm alone. The formula is specific to the fourth moment, with modest scope honestly stated; no downstream theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
