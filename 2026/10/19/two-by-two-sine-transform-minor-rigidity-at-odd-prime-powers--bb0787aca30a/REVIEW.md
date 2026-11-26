# Independent mathematical audit

## correctness

PASS

For the unnormalized inversion-odd kernel the determinant numerator has augmentation zero and coefficient l1 norm at most 8, after reducing its exponents modulo N. At N=p^k cyclotomic divisibility gives P=Phi_N Q with integral Q of degree below p^(k-1), making coefficient fibers disjoint. Nonzero Q has augmentation zero and l1 norm at least 2, giving a contradiction for p>=5. In the formal product identity V_a V_b=C_(a+b)-C_(a-b), the signed supports are distinct unless a or b is zero (2 is invertible); C_0 has coefficient 2 at 0, and causes no ambiguity of support. Matching the two nonzero terms separately gives a simultaneous sign with or without swapping the factors, hence A or B, while two zero products give C. All three alternatives give vanishing. At p^2, if neither pair is all divisible, at most one entry can vanish and the unit in each pair forces signed congruence modulo p^2 of distinct signed representatives, which is impossible. With an all-divisible pair, the other can be all divisible, mixed, or an all-unit pair in the same signed residue class modulo p; each of the d=(p-1)/2 classes has p unit representatives. The disjoint count h^2+2hd(pd+binom(p,2)), h=binom(d,2), simplifies as claimed and the total-minor denominator is asymptotic to p^8/64. A separate exact replay at N=9 gave all 36 nonzero determinants at zeta=4 of order 9 in F_19, with Phi_9(4)=0; this is a valid specialization certificate (replay: /workspace/branches/0cdaf4d3-ec94-4db6-9c4c-2fe2a5487011/replay_n9.py and replay_n9.out). The frozen verifier and output were inspected, not rerun. No p=3 classification beyond N=9 is needed or accepted here.

## originality

PASS

The positive determination is for the exact composite prime-power criterion and prime-square incidence count. Prime order nonvanishing, composite order zero entries, and general cyclotomic vanishing-sum tools are prior; none of the material inspected asserts or immediately yields the full compound claim.

## value

PASS

For a natural Fourier compression, the smallest nontrivial minors measure exact two-row dependence on chosen columns. A complete arithmetic test distinguishes structural zeros from possible cancellations and quantifies their rarity at prime squares. The order-9 replay is only a boundary certificate; value rests on the general classification and count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
