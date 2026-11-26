# Independent mathematical audit

## correctness

PASS

For the basis identification e_i↔X^i mod X^n−1, the product is σ_{−1}(f)σ_2(g). The two substitutions are F_q-algebra automorphisms since n is odd. Composition with an automorphism on the right and conjugation of an ordinary multiplication operator preserve rank, so both ranks equal rank M_a pointwise. With J=(X^m−1) in the quotient, its p^s-th power is zero and B/J is the product of residue fields from the distinct factors. For T=M_bσ, T^h=M_{∏_{t<h}σ^t(b)}σ^h. On a quotient cycle with no zero b-coordinate T is bijective there, so T cannot be nilpotent. If each cycle has a zero, take h the order of the factor permutation; the product then lies in J despite possible nontrivial automorphisms inside the fields. Repeating the exact product p^s times puts its multiplier in J^(p^s)=0. This works even if m=1 or p divides h; no division by a cycle length is needed. On each cycle the choices are precisely all tuples minus the all-nonzero tuples, followed by the uniform radical fiber of size q^(n−m). The bijections a↦σ_{−1}(a), σ_2(a) give the two counts. At (n,q)=(5,11), nontrivial split factors form one 4-cycle under doubling and two 2-cycles under inversion, giving 4641 and 441. At (7,2) squaring acts trivially on the three Frobenius classes and inversion swaps the two cubic factors, giving 1 and 15. Independently enumerated all 128 and 27 coefficient vectors at (7,2) and the modular (3,3), respectively: form columns by the basis product, apply each matrix n times to all basis vectors, and independently row-reduce over the prime field. Nilpotent counts were (1,15) and (9,9), with no rank mismatch; e_0+e_1+e_2+e_4 at (7,2) has both ranks 3 and only R_a nilpotent. These checks are finite corroboration. Read the frozen verifier sources but did not run them. checker_output.txt is the rank transcript, and the nil_output.txt referenced in VERIFICATION.md was not present; the recorded claim about the latter is not used as evidence of a run.

## originality

PASS

Credit attaches to the left/right operator-nilpotency counts, modular lift, and two directions of the disparity. The Alexander product transport is prior work and pointwise equal rank is a direct consequence of it in this case; neither is credited as an original contribution. Indexed rank spectra and product-nilpotency results overlap in language or method but do not determine the factor-cycle condition for operator powers.

## value

PASS

Operator nilpotence is a natural invariant not recoverable from the known ranks. The exact orbit formula accounts for all odd orders and all finite fields, shows explicitly what modular reduction does and does not change, and produces witnesses that reverse which operator is more often nilpotent. This is more informative than a small rank-versus-nilpotence counterexample alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
