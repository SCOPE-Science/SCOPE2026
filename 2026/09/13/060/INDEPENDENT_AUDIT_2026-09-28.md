# Independent audit — SCOPE-20260913-060

Date: 2026-09-28 (UTC)  

## Disposition: PASSED

### Correctness
The witness proof is sound. The torsion theorem gives x=R^3 and y=aR^3a^-1 as involutions. The stated S4 quotient sends R^3 to (0 2)(1 3) and y to (0 3)(1 2), so they are distinct. If t=xy had finite order, it would be conjugate to R^k; t and t^-1 are conjugate via x, forcing 2k[R]=0 in the abelianization where [R] has order six, hence k=0 or 3. k=0 contradicts x!=y, while k=3 contradicts [t]=0 versus [R^3]!=0. Therefore t has infinite order and <x,y> is D_infinity.

### Originality
The general CSA criterion and torsion structure are classical; the contribution is the explicit witness and elementary abelianization/S4 separation for this particular relator. Originality is therefore limited-to-moderate and instance-specific.

### Scientific value
The record decisively resolves the target group by an explicit certificate that is easy to recheck and avoids a black-box subgroup search.

### Sources checked
- Gildenhuys, Kharlampovich and Myasnikov, CSA-groups and separated free constructions: https://doi.org/10.1017/S0004972700014453 — States that a one-relator group with torsion is CSA iff it contains no infinite dihedral subgroup.

### Limitations
- The classical one-relator torsion theorem is quoted rather than reproved.
- No claim is made about the full subgroup lattice or other geometric properties of G3.
