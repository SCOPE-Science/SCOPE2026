# Independent mathematical audit

## correctness

PASS

The rational generating functions split each extraction fraction into the integer prefix ending in X_n or Y_n plus a positive tail T_n or U_n. At b_X=2a(a+1)-1 and b_Y=2a(y+1), the recurrence bounds in the package make the corresponding tails less than one for every n and keep each coordinate below the modulus. For a smaller positive-denominator base, if the n=1 tail does not already change the residue, it must hide a positive multiple of b; the resulting bounds on s=b-2a force the n=2 tail strictly between one and b^2, so it cannot disappear modulo b^2. This proves exact coordinate-wise minimality rather than only sufficiency. An independent replay on nonsquare d in {2,3,5,6,7,10,11} exhausted every smaller manageable base and verified both thresholds through n=6, reproducing for d=7 the pair 143 and 64. The inspected package verifier independently performs a much larger finite corroboration while the all-d theorem rests on the symbolic tail proof.

## originality

PASS

Dumitru--Prunescu prove that 2X1(X1+1)-1 is the least common base for the two formulas, explicitly using the two coordinates together. Prunescu--Sauras-Altuzarra give the formulas for sufficiently large bases and, in Example 38, the d=7 choices 143 for X and 64 for Y. The relevant primary pages of both papers were read: neither states a general least Y-coordinate base 2X1(Y1+1), nor a general coordinate-wise minimality theorem. The X-coordinate optimum agrees with the already-known common optimum; the accepted originality is the separation of the optimization problems and especially the exact general Y threshold, together with the n=2 obstruction that proves sharpness.

## value

PASS

The exact base is the natural resource parameter of the published coefficient-extraction formulas. Separating the two coordinates reveals that the Y formula can have a substantially smaller sharp base than the common threshold, while the X formula already forces the common optimum; this is an exact reusable refinement of a current arithmetic-representation construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
