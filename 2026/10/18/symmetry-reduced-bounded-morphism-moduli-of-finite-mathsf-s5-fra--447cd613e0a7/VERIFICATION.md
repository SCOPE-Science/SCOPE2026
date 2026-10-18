---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification evidence

All programs use Python standard library only. In a directory containing the three included scripts, run:

```sh
python s5_orbit_direct.py
python s5_orbit_full_group.py
python s5_orbit_burnside.py
```

The first compares the exact formula with actual enumeration of all functions on every source/target isomorphism type considered (278 frame pairs). The second explicitly enumerates both automorphism groups and acts on the actual function set (55 frame pairs). The third is the exact formula calculator; its default mode emits exact counts for all 278 pairs. Additionally, the included `family_checks.txt` records comparisons for three closed parameter families on 45 instances. These are finite checks, not proof of the unrestricted theorem. See `RESULT.md` for the all-parameter proof and scientific limitations.

Expected summaries: `ALL PASS 278 source/target frame pairs, all functions checked up to six source worlds and four target worlds`; `ALL PASS 55 complete source-and-target automorphism-action instances; 175 surjective bounded maps`; `ALL PASS three closed families, r=1..15 (45 evaluations)`.
