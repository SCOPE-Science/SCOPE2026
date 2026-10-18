# Independent mathematical audit

## correctness

PASS

For every c>=2 except 4 and every nonzero integral conic point, source quotient formulas z1=cx+y+c, z2=cz1+x+c, z3=cz2+z1-c, z4=cz3+z2-c obey P0(x)=y z1, P1(z1)=x z2, P2(z2)=z1 z3, P3(z3)=z2 z4 on C=x^2-y^2+c(x-y)+c-cxy=0, and (z4,z3) preserves C. Independent SymPy exact division verifies all four identities are +/-C and return conic is C. Nonzero quotients follow because c(c-4) and c(c+4) cannot be nonzero-square discriminants of P0,P2 or P1,P3: factor pairs of 4 of same parity force c=4 or c=0 respectively. Induction proves indefinite continuation for c!=4. At c=4 point (-2,4) lies on C and z1=0. No positivity/coprimality hypothesis used.

## originality

PASS

PASS, best of knowledge: Alekseyev-Khomovsky Proposition 4.12 constructs infinitely many positive unit-class points and gives the same recurrences and invariant, while Proposition 4.11 imposes an S-coprime chamber for a general sufficient criterion. Proposition 4.13 linearizes the coefficient/Pell dynamics but does not prove all nonzero integral points avoid zero quotient or isolate the unique c=4 failure. The assessed root-exclusion and full all-point lifting are additional.

## value

PASS

PASS: removes an explicit arithmetic chamber restriction from a nonunit normalized quadratic divisibility cycle and identifies a sharp exceptional integer parameter, a structural boundary of the original paper’s lifting question. Nonzero solutions outside the positive coprime chamber can now be classified as indefinitely liftable for all c!=4.

The dated certificate retains the supplied scientific assessment, sources and limitations.
