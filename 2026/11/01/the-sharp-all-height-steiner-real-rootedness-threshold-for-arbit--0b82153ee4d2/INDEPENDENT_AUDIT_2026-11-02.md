# Independent mathematical audit

## correctness

PASS

For any compact planar convex base of area A>0 and perimeter P, direct slicing the 3D outer parallel body gives Vol(K_h+t B_3)=hA+(hP+2A)t+(pi h+pi P/2)t²+(4pi/3)t³. Using ell=P/(2pi), u=h/ell, z=t/ell and q=4pi A/P² yields F=4z³/3+(u+pi)z²+2(u+q)z+qu, for 0<q<=1. Put r=3(pi-4)/2 and q*=-r²-2r=15pi-9pi²/4-24≈0.9172799013958417. For q<q*, Bq=z²+2z+q has negative roots beta1<r<beta2<0; evaluation F(beta_i)=-(2/3) beta_i² (beta_i-r) gives three strict sign changes in disjoint negative intervals for every u>0. At q=q*, exact factorization F=(z-r)[4z²/3+(u+3pi-8)z+u(3pi/2-4)] has two distinct negative quadratic roots and precisely one u=u*≈0.6537122861709328 where r coincides as a double root, never triple. At that same u*, independently derived cubic discriminant as delta=q-q*: C1 delta+C2 delta²-(128/3)delta³, C1,C2<0 using exact formulas and certified pi bounds, so every q>q* gives one negative real root plus conjugate nonreal pair. Independent SymPy reconstruction checked critical/discriminant identities and the q6<q*<q7 regular polygon crossover. No finite random root sample is used as a proof.

## originality

PASS

The general Steiner polynomial product formula is established prior work (Katsnelson 2008). Henk–Hernández Cifre 2008 and Henk–Hernández Cifre–Saorín 2012 give root-location/cone restrictions, but the inspected statements do not identify this exact prism-specific isoperimetric quotient frontier. Saorín Gómez (2008) thesis Example 1.3 is direct same-family specialization for circular cylinders (q=1): its root regimes do not imply the all-base all-height threshold and base-independent witness, or the regular six-to-seven polygon cutoff. Full primary thesis example and relevant source theorem pages were directly inspected. Resultary returned a theorem for right circular cones, an essentially different volume polynomial.

## value

PASS

Ordinary Steiner cubic root geometry of 3D convex bodies is a standard structural problem. The result gives a complete all-positive-height real-rootedness classification simultaneously for every planar convex base using one natural isoperimetric invariant q, including a sharp universal normalized witness height for all excluded shapes. The regular m-gon threshold between six and seven sides supplies a clear natural family cutoff, not arbitrary computational slices. This theorem is nontrivial beyond the classical product-coefficient calculation or isolated circular-cylinder case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
